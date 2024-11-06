from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.conf import settings


class Command(BaseCommand):
    help = "Load all YAML fixtures from each app's fixtures directory inside the apps folder."

    def handle(self, *args, **options):
        base_apps_dir = Path(settings.BASE_DIR) / 'apps'

        for app_dir in base_apps_dir.iterdir():
            if not app_dir.is_dir():
                continue
            fixtures_dir = app_dir / 'fixtures'
            if not fixtures_dir.exists() or not fixtures_dir.is_dir():
                continue
            # Find all .yaml files in the fixtures directory
            yaml_files = list(fixtures_dir.glob('*.yaml'))
            if not yaml_files:
                self.stdout.write(self.style.WARNING(f'No YAML fixtures found in {fixtures_dir}.'))
                continue

            # Load each YAML file in the fixtures directory
            for yaml_file in yaml_files:
                fixture_name = yaml_file.name
                self.stdout.write(f'Loading fixture {fixture_name} from {fixtures_dir}...')

                try:
                    call_command('loaddata', str(yaml_file))
                    self.stdout.write(self.style.SUCCESS(f'Successfully loaded {fixture_name}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Failed to load {fixture_name}: {e}'))
