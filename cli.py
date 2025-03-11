import os
import click
from pathlib import Path

# Define the template directory
TEMPLATE_DIR = Path(__file__).parent / "templates"


@click.group()
def cli():
    """Flask CLI for generating new projects"""
    pass


@cli.command("new")
@click.option("--template", default="demo_template", help="Template name")
def create_project(template):
    """Create a new Flask project with a default structure."""
    project_name = click.prompt("Enter your project name", default="my_flask_app")

    if os.path.exists(project_name):
        click.echo("❌ Project already exists!")
        return

    click.echo(f"🚀 Creating Flask project: {project_name}...")

    # Define directory structure
    project_structure = {
        "app": [
            "config.py",
            "__init__.py",
            "models.py",
            "views.py",
        ],
        "app/static": [
            "style.css",
        ],
        "app/templates": [
            "base.html",
            "index.html",
            "about.html",
        ],
        "app/__pycache__": [],
    }

    # Create directories and files
    for folder, files in project_structure.items():
        folder_path = Path(project_name) / folder
        folder_path.mkdir(parents=True, exist_ok=True)

        for file in files:
            template_path = TEMPLATE_DIR / f"{file}.template"
            file_path = folder_path / file

            if template_path.exists():
                file_content = template_path.read_text()
                file_path.write_text(file_content)
                click.echo(f"📄 Created: {file_path}")
            else:
                file_path.touch()  # Create empty file if no template exists
                click.echo(f"📂 Created empty file: {file_path}")

    # Create top-level files
    top_level_files = ["run.py",  "README.md", "requirements.txt"]
    for file in top_level_files:
        template_path = TEMPLATE_DIR / f"{file}.template"
        file_path = Path(project_name) / file

        if template_path.exists():
            file_content = template_path.read_text()
            file_path.write_text(file_content)
            click.echo(f"📄 Created: {file_path}")
        else:
            file_path.touch()  # Create empty file if no template exists
            click.echo(f"📂 Created empty file: {file_path}")

    # Create .env file
    env_template_path = TEMPLATE_DIR / ".env.template"
    env_file_path = Path(project_name) / ".env"

    if env_template_path.exists():
        env_content = env_template_path.read_text()
        env_file_path.write_text(env_content)
        click.echo(f"📄 Created: {env_file_path}")
    else:
        # Create a default .env file if no template exists
        default_env_content = """# Flask Environment Variables
PROJECT_NAME=My Flask Blog
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///app.db
DEBUG=True
"""
        env_file_path.write_text(default_env_content)
        click.echo(f"📂 Created default .env file: {env_file_path}")

    click.echo(f"\n✅ Flask project '{project_name}' created successfully!")


if __name__ == "__main__":
    cli()
