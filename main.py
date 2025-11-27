#!/usr/bin/env python3
"""
Manim Animation Studio - Project & Rendering Manager

An interactive interface for loading Manim projects and rendering animations.
Projects are created by Claude Code in the manim-projects/ directory.

Usage:
    python main.py                    # Start interactive session
    python main.py --project myproj   # Load specific project
    python main.py --list             # List all projects

Workflow:
    1. Use Claude Code to create animation projects
    2. Run this interface to select projects and render scenes
    3. Choose which scene to render interactively

Note: This interface is for project selection and rendering only.
      Use Claude Code for all animation creation and refinement.
"""

import os
import sys
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import readline  # For better input editing


class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ManimStudio:
    """Project manager for Manim animations - rendering and file organization"""

    def __init__(self, workspace_dir: str = "manim-projects"):
        # Convert to absolute path to avoid issues when changing directories
        self.workspace_dir = Path(workspace_dir).resolve()
        self.workspace_dir.mkdir(exist_ok=True)
        self.current_project: Optional[str] = None
        self.project_dir: Optional[Path] = None
        self.session_file: Optional[Path] = None

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name != 'nt' else 'cls')

    def print_banner(self):
        """Print welcome banner"""
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
TPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPW
Q                                                              Q
Q            <� MANIM ANIMATION STUDIO <�                      Q
Q                                                              Q
Q     Project Manager for Manim Animations                    Q
Q     Use with Claude Code for animation generation           Q
Q                                                              Q
ZPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP]
{Colors.ENDC}
"""
        print(banner)

    def print_help(self):
        """Print help information"""
        help_text = f"""
{Colors.BOLD}Available Commands:{Colors.ENDC}

  {Colors.GREEN}/load{Colors.ENDC}             - Load a project (interactive selection)
  {Colors.GREEN}/list{Colors.ENDC}             - List all projects
  {Colors.GREEN}/info{Colors.ENDC}             - Show current project info
  {Colors.GREEN}/files{Colors.ENDC}            - Show files in current project
  {Colors.GREEN}/render{Colors.ENDC}           - Render animation (select project, scene, or combined video)
  {Colors.GREEN}/preview{Colors.ENDC}          - Quick preview (low quality, select scene)
  {Colors.GREEN}/clear{Colors.ENDC}            - Clear screen
  {Colors.GREEN}/help{Colors.ENDC}             - Show this help
  {Colors.GREEN}/exit{Colors.ENDC} or {Colors.GREEN}/quit{Colors.ENDC} - Exit the studio

{Colors.BOLD}Working with Claude Code:{Colors.ENDC}

  1. Use Claude Code to create animation projects in manim-projects/
  2. Load a project with {Colors.GREEN}/load{Colors.ENDC}
  3. Use {Colors.GREEN}/render{Colors.ENDC} or {Colors.GREEN}/preview{Colors.ENDC} to render scenes
     → Option -1: Combined video (all scenes in one file)
     → Option 0: All scenes (separate files)
     → Option 1+: Individual scenes
  4. Ask Claude to refine animations based on rendered output

{Colors.BOLD}Tips:{Colors.ENDC}
  " Projects are in manim-projects/ (one directory per project)
  " Each project has animation.py, params.py, README.md
  " Combined videos are created using ffmpeg (requires ffmpeg installed)
  " Use Claude Code for all animation creation and refinement
  " This interface is for project selection and rendering only
"""
        print(help_text)

    def list_projects(self) -> List[str]:
        """List all existing projects"""
        if not self.workspace_dir.exists():
            return []

        projects = []
        for item in self.workspace_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                projects.append(item.name)

        return sorted(projects)

    def print_projects(self):
        """Print list of all projects"""
        projects = self.list_projects()

        if not projects:
            print(f"\n{Colors.YELLOW}No projects found yet.{Colors.ENDC}")
            print(f"Use {Colors.GREEN}/new [name]{Colors.ENDC} to create your first project!\n")
            return

        print(f"\n{Colors.BOLD}=� Available Projects:{Colors.ENDC}\n")
        for i, project in enumerate(projects, 1):
            project_path = self.workspace_dir / project
            session_file = project_path / "session.json"

            # Get project info
            created = datetime.fromtimestamp(project_path.stat().st_ctime)
            modified = datetime.fromtimestamp(project_path.stat().st_mtime)

            # Count files
            files = list(project_path.glob("*.py"))
            reports = list((project_path / "research-reports").glob("*.md")) if (project_path / "research-reports").exists() else []

            active = " (CURRENT)" if project == self.current_project else ""

            print(f"  {Colors.CYAN}{i}. {project}{Colors.ENDC}{Colors.GREEN}{active}{Colors.ENDC}")
            print(f"     Created: {created.strftime('%Y-%m-%d %H:%M')}")
            print(f"     Files: {len(files)} Python, {len(reports)} Reports")
            print()

    def create_project(self, name: str):
        """Create a new project"""
        # Sanitize project name
        name = name.strip().replace(' ', '-').lower()

        if not name:
            print(f"{Colors.RED}Error: Project name cannot be empty{Colors.ENDC}")
            return False

        project_path = self.workspace_dir / name

        if project_path.exists():
            print(f"{Colors.YELLOW}Project '{name}' already exists.{Colors.ENDC}")
            response = input(f"Load it instead? (y/n): ").strip().lower()
            if response == 'y':
                return self.load_project(name)
            return False

        # Create project structure
        project_path.mkdir(parents=True)
        (project_path / "research-reports").mkdir()

        # Initialize session file
        session_data = {
            "name": name,
            "created": datetime.now().isoformat(),
            "last_accessed": datetime.now().isoformat(),
            "files": [],
            "status": "active"
        }

        session_file = project_path / "session.json"
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)

        # Create README
        readme = project_path / "README.md"
        with open(readme, 'w') as f:
            f.write(f"# {name.title()}\n\n")
            f.write(f"Created: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write("## Project Files\n\n")
            f.write("- Animation code: `*.py`\n")
            f.write("- Research reports: `research-reports/*.md`\n")
            f.write("- Session history: `session.json`\n\n")
            f.write("## Rendering\n\n")
            f.write("```bash\n")
            f.write("# Preview (low quality)\n")
            f.write("manim -pql [file].py [Scene]\n\n")
            f.write("# High quality\n")
            f.write("manim -pqh [file].py [Scene]\n")
            f.write("```\n")

        self.current_project = name
        self.project_dir = project_path
        self.session_file = session_file

        print(f"\n{Colors.GREEN} Created new project: {name}{Colors.ENDC}")
        print(f"{Colors.CYAN}Location: {project_path}{Colors.ENDC}\n")

        return True

    def load_project(self, name: str) -> bool:
        """Load an existing project"""
        project_path = self.workspace_dir / name

        if not project_path.exists():
            print(f"{Colors.RED}Error: Project '{name}' not found{Colors.ENDC}")
            return False

        session_file = project_path / "session.json"

        if not session_file.exists():
            print(f"{Colors.YELLOW}Warning: session.json not found, creating new one{Colors.ENDC}")
            session_data = {
                "name": name,
                "created": datetime.now().isoformat(),
                "last_accessed": datetime.now().isoformat(),
                "files": [],
                "status": "active"
            }
        else:
            with open(session_file, 'r') as f:
                session_data = json.load(f)

        # Update last accessed
        session_data["last_accessed"] = datetime.now().isoformat()

        self.current_project = name
        self.project_dir = project_path
        self.session_file = session_file

        # Save updated session
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)

        print(f"\n{Colors.GREEN} Loaded project: {name}{Colors.ENDC}")
        print(f"{Colors.CYAN}Location: {project_path}{Colors.ENDC}\n")

        return True

    def save_session(self):
        """Save current session state"""
        if not self.session_file:
            return

        session_data = {
            "name": self.current_project,
            "created": datetime.now().isoformat(),  # Default to current time
            "last_accessed": datetime.now().isoformat(),
            "files": self._get_project_files(),
            "status": "active"
        }

        # Preserve creation date if exists
        if self.session_file.exists():
            try:
                with open(self.session_file, 'r') as f:
                    existing = json.load(f)
                    session_data["created"] = existing.get("created", datetime.now().isoformat())
            except (json.JSONDecodeError, IOError):
                pass  # Keep default creation time if file is corrupt

        # Ensure parent directory exists
        self.session_file.parent.mkdir(parents=True, exist_ok=True)

        with open(self.session_file, 'w') as f:
            json.dump(session_data, f, indent=2)

    def _get_project_files(self) -> List[str]:
        """Get list of files in current project"""
        if not self.project_dir:
            return []

        files = []
        for ext in ['*.py', '*.md']:
            files.extend([str(f.relative_to(self.project_dir)) for f in self.project_dir.rglob(ext)])

        return sorted(files)

    def show_project_info(self):
        """Show information about current project"""
        if not self.current_project:
            print(f"{Colors.YELLOW}No project loaded. Use /new or /load{Colors.ENDC}")
            return

        print(f"\n{Colors.BOLD}=� Project Information{Colors.ENDC}\n")
        print(f"  Name: {Colors.CYAN}{self.current_project}{Colors.ENDC}")
        print(f"  Location: {Colors.CYAN}{self.project_dir}{Colors.ENDC}")

        # Count files
        py_files = list(self.project_dir.glob("*.py"))
        reports_dir = self.project_dir / "research-reports"
        reports = list(reports_dir.glob("*.md")) if reports_dir.exists() else []

        print(f"  Python files: {len(py_files)}")
        print(f"  Research reports: {len(reports)}")
        print()

    def show_files(self):
        """Show files in current project"""
        if not self.current_project:
            print(f"{Colors.YELLOW}No project loaded.{Colors.ENDC}")
            return

        print(f"\n{Colors.BOLD}=� Project Files{Colors.ENDC}\n")

        # Python files
        py_files = sorted(self.project_dir.glob("*.py"))
        if py_files:
            print(f"{Colors.CYAN}Animation Code:{Colors.ENDC}")
            for f in py_files:
                size = f.stat().st_size
                print(f"  {f.name} ({size:,} bytes)")

        # Research reports
        reports_dir = self.project_dir / "research-reports"
        if reports_dir.exists():
            reports = sorted(reports_dir.glob("*.md"))
            if reports:
                print(f"\n{Colors.CYAN}Research Reports:{Colors.ENDC}")
                for f in reports:
                    size = f.stat().st_size
                    print(f"  {f.name} ({size:,} bytes)")

        # Media files (if any)
        media_dir = self.project_dir / "media"
        if media_dir.exists():
            videos = list(media_dir.rglob("*.mp4"))
            if videos:
                print(f"\n{Colors.CYAN}Rendered Videos:{Colors.ENDC}")
                for f in videos[:5]:  # Show first 5
                    size = f.stat().st_size / (1024 * 1024)  # MB
                    print(f"  {f.relative_to(media_dir)} ({size:.1f} MB)")

        print()

    def get_scenes_from_file(self, py_file: Path) -> List[str]:
        """Extract scene class names from a Python file"""
        scenes = []
        try:
            with open(py_file, 'r') as f:
                for line in f:
                    # Look for class definitions that inherit from Scene
                    if 'class ' in line and '(Scene)' in line:
                        # Extract class name
                        class_name = line.split('class ')[1].split('(')[0].strip()
                        scenes.append(class_name)
        except Exception as e:
            print(f"{Colors.RED}Error reading file: {e}{Colors.ENDC}")

        return scenes
    
    def find_output_video_dir(self, py_file: Path):
        """Find the Manim output directory for a given Python file.
        Manim creates: media/videos/<filename_without_extension>/<quality>/

        NOTE: This assumes we're already in the project directory (after os.chdir).
        """
        # Get filename without extension (e.g., "animation" from "animation.py")
        filename_stem = py_file.stem

        # Build path from current directory (we're already in project_dir after chdir)
        media_videos = Path("media") / "videos" / filename_stem

        if not media_videos.exists():
            return None

        # Accept these quality folders
        qualities = ["1080p60", "720p30", "480p15", "2160p60"]

        # Check for any quality folder
        for quality in qualities:
            quality_dir = media_videos / quality
            if quality_dir.exists():
                return quality_dir

        return None


    def render_animation(self, quick: bool = False):
        """Render the animation with correct handling and no accidental Path→str conversion."""
        # Step 1: Select project
        if not self.current_project:
            projects = self.list_projects()
            if not projects:
                print(f"{Colors.RED}No projects found in manim-projects/{Colors.ENDC}")
                return

            print(f"\n{Colors.BOLD}Select Project:{Colors.ENDC}\n")
            for i, p in enumerate(projects, 1):
                print(f"  {Colors.CYAN}{i}. {p}{Colors.ENDC}")

            choice = input(f"\n{Colors.BOLD}Project: {Colors.ENDC}").strip()
            try:
                project_name = projects[int(choice) - 1]
                if not self.load_project(project_name):
                    return
            except:
                print(f"{Colors.RED}Invalid choice.{Colors.ENDC}")
                return

        # Step 2: Python files
        py_files = list(self.project_dir.glob("*.py"))
        if not py_files:
            print(f"{Colors.RED}No Python files found.{Colors.ENDC}")
            return

        # Step 3: Select file
        if len(py_files) == 1:
            file_to_render = py_files[0]  # Path object
        else:
            print(f"\n{Colors.BOLD}Select Animation File:{Colors.ENDC}\n")
            for i, f in enumerate(py_files, 1):
                print(f"  {Colors.CYAN}{i}. {f.name}{Colors.ENDC}")

            choice = input(f"\n{Colors.BOLD}File: {Colors.ENDC}").strip()
            try:
                file_to_render = py_files[int(choice) - 1]  # Path object
            except:
                print(f"{Colors.RED}Invalid choice.{Colors.ENDC}")
                return

        # Path object stays a Path object
        filename = file_to_render.name  # string passed to manim

        # Step 4: Scene list
        scenes = self.get_scenes_from_file(file_to_render)
        if not scenes:
            print(f"{Colors.RED}No Scene classes found.{Colors.ENDC}")
            return

        # Step 5: Scene selection
        print(f"\n{Colors.BOLD}Select Scene:{Colors.ENDC}\n")
        print(f"  {Colors.CYAN}-1. Combined video (no popups){Colors.ENDC}")
        print(f"  {Colors.CYAN} 0. All scenes separately{Colors.ENDC}")
        for i, s in enumerate(scenes, 1):
            print(f"  {Colors.CYAN}{i}. {s}{Colors.ENDC}")

        choice = input(f"\n{Colors.BOLD}Scene: {Colors.ENDC}").strip()
        try:
            idx = int(choice)
        except:
            print(f"{Colors.RED}Invalid choice.{Colors.ENDC}")
            return

        quality = "l" if quick else "h"

        os.chdir(self.project_dir)

        # --------------------------- CASE -1: Combined video -----------------------------
        if idx == -1:
            # IMPORTANT: no -p (so no scenes pop up)
            cmd = f"manim -q{quality} {filename}"
            print(f"\n{Colors.GREEN}→ Rendering combined video (no auto-play){Colors.ENDC}")
            print(f"{Colors.CYAN}Running: {cmd}{Colors.ENDC}")
            os.system(cmd)

            media_dir = self.find_output_video_dir(file_to_render)
            if not media_dir:
                print(f"{Colors.RED}No output directory found.{Colors.ENDC}")
                return

            videos = list(media_dir.glob("*.mp4"))
            if not videos:
                print(f"{Colors.RED}No output video found.{Colors.ENDC}")
                return

            print(f"\n{Colors.GREEN}✓ Combined video complete!{Colors.ENDC}")
            print(f"{Colors.CYAN}→ Saved as:{Colors.ENDC}  {videos[-1]}")
            return

        # --------------------------- CASE 0: Separate videos -----------------------------
        if idx == 0:
            print(f"\n{Colors.GREEN}→ Rendering each scene separately...{Colors.ENDC}")
            for scene in scenes:
                cmd = f"manim -pq{quality} {filename} {scene}"
                print(f"{Colors.CYAN}Running: {cmd}{Colors.ENDC}")
                os.system(cmd)

            media_dir = self.find_output_video_dir(file_to_render)
            if media_dir:
                print(f"\n{Colors.GREEN}✓ All scenes rendered separately!{Colors.ENDC}")
                print(f"{Colors.CYAN}→ Saved in:{Colors.ENDC}  {media_dir}")
            else:
                print(f"\n{Colors.YELLOW}Rendering complete, but output directory not found.{Colors.ENDC}")
            return

        # --------------------------- CASE 1..n: Single scene -----------------------------
        if 1 <= idx <= len(scenes):
            scene = scenes[idx - 1]
            cmd = f"manim -pq{quality} {filename} {scene}"
            print(f"\n{Colors.GREEN}→ Rendering scene: {scene}{Colors.ENDC}")
            print(f"{Colors.CYAN}Running: {cmd}{Colors.ENDC}")
            os.system(cmd)

            media_dir = self.find_output_video_dir(file_to_render)
            if media_dir:
                output = media_dir / f"{scene}.mp4"
                if output.exists():
                    file_size = output.stat().st_size / (1024 * 1024)  # MB
                    print(f"\n{Colors.GREEN}✓ Render complete!{Colors.ENDC}")
                    print(f"{Colors.CYAN}→ Saved as:{Colors.ENDC}  {output}")
                    print(f"{Colors.CYAN}  Size: {file_size:.1f} MB{Colors.ENDC}")
                else:
                    print(f"\n{Colors.YELLOW}Rendering complete, but video file not found at expected location.{Colors.ENDC}")
            else:
                print(f"\n{Colors.YELLOW}Rendering complete, but output directory not found.{Colors.ENDC}")
            return

        print(f"{Colors.RED}Invalid choice.{Colors.ENDC}")



    def run(self):
        """Main interactive loop"""
        self.clear_screen()
        self.print_banner()

        print(f"{Colors.YELLOW}Welcome to Manim Animation Studio!{Colors.ENDC}")
        print(f"Type {Colors.GREEN}/help{Colors.ENDC} for commands.\n")
        print(f"{Colors.CYAN}Use Claude Code to create animation projects.{Colors.ENDC}")
        print(f"{Colors.CYAN}Use {Colors.GREEN}/load{Colors.ENDC} to select a project and {Colors.GREEN}/render{Colors.ENDC} to render scenes.{Colors.ENDC}\n")

        # Auto-load last project if exists
        projects = self.list_projects()
        if projects:
            print(f"Found {len(projects)} existing project(s).")
            load_last = input(f"Load most recent project '{projects[-1]}'? (y/n): ").strip().lower()
            if load_last == 'y':
                self.load_project(projects[-1])
            else:
                print(f"Use {Colors.GREEN}/load{Colors.ENDC} to select a project.\n")
        else:
            print(f"{Colors.YELLOW}No projects found yet.{Colors.ENDC}")
            print(f"{Colors.CYAN}Use Claude Code to create your first project in manim-projects/{Colors.ENDC}\n")

        # Main chat loop
        while True:
            try:
                # Prompt
                if self.current_project:
                    prompt = f"{Colors.BOLD}{self.current_project}{Colors.ENDC} > "
                else:
                    prompt = f"{Colors.BOLD}manim-studio{Colors.ENDC} > "

                user_input = input(prompt).strip()

                if not user_input:
                    continue

                # Handle commands
                if user_input.startswith('/'):
                    self._handle_command(user_input)
                else:
                    # Inform user to use Claude Code for animation requests
                    print(f"\n{Colors.CYAN}→ For animation creation and refinement, use Claude Code.{Colors.ENDC}")
                    print(f"{Colors.YELLOW}This interface only supports commands (type /help).{Colors.ENDC}\n")

            except KeyboardInterrupt:
                print(f"\n\n{Colors.YELLOW}Use /exit to quit{Colors.ENDC}\n")
            except EOFError:
                break

        print(f"\n{Colors.CYAN}Goodbye! Happy animating! <�{Colors.ENDC}\n")

    def _handle_command(self, command: str):
        """Handle slash commands"""
        parts = command.split(maxsplit=1)
        cmd = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        if cmd in ['/exit', '/quit']:
            print(f"\n{Colors.CYAN}Saving session...{Colors.ENDC}")
            self.save_session()
            print(f"{Colors.GREEN} Session saved{Colors.ENDC}")
            print(f"{Colors.CYAN}Goodbye! <�{Colors.ENDC}\n")
            sys.exit(0)

        elif cmd == '/help':
            self.print_help()

        elif cmd == '/clear':
            self.clear_screen()
            self.print_banner()

        elif cmd == '/load':
            projects = self.list_projects()
            if not projects:
                print(f"\n{Colors.YELLOW}No projects found.{Colors.ENDC}")
                print(f"{Colors.CYAN}Use Claude Code to create projects in manim-projects/{Colors.ENDC}\n")
                return

            print(f"\n{Colors.BOLD}Select Project to Load:{Colors.ENDC}\n")
            for i, project in enumerate(projects, 1):
                active = " (CURRENT)" if project == self.current_project else ""
                print(f"  {Colors.CYAN}{i}. {project}{Colors.ENDC}{Colors.GREEN}{active}{Colors.ENDC}")

            choice = input(f"\n{Colors.BOLD}Project (1-{len(projects)}): {Colors.ENDC}").strip()
            try:
                project_name = projects[int(choice) - 1]
                self.load_project(project_name)
            except (ValueError, IndexError):
                print(f"{Colors.RED}Invalid choice.{Colors.ENDC}")

        elif cmd == '/list':
            self.print_projects()

        elif cmd == '/info':
            self.show_project_info()

        elif cmd == '/files':
            self.show_files()

        elif cmd == '/render':
            self.render_animation(quick=False)

        elif cmd == '/preview':
            self.render_animation(quick=True)

        else:
            print(f"{Colors.RED}Unknown command: {cmd}{Colors.ENDC}")
            print(f"Type {Colors.GREEN}/help{Colors.ENDC} for available commands")


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description="Manim Animation Studio - Project Manager")
    parser.add_argument('--project', '-p', help='Load specific project')
    parser.add_argument('--list', '-l', action='store_true', help='List all projects')
    parser.add_argument('--workspace', '-w', default='manim-projects', help='Workspace directory')

    args = parser.parse_args()

    studio = ManimStudio(workspace_dir=args.workspace)

    if args.list:
        studio.print_projects()
        return

    if args.project:
        if not studio.load_project(args.project):
            print(f"\n{Colors.RED}Project '{args.project}' not found.{Colors.ENDC}")
            print(f"{Colors.CYAN}Use Claude Code to create it first, or use /load to select from existing projects.{Colors.ENDC}\n")

    studio.run()


if __name__ == "__main__":
    main()
