from rich.console import Console
from rich.live import Live
from rich.console import Group
import time
import monitor
import ui

console = Console()

def gather_stats():
    return {
        "cpu": monitor.cpu_usage(),
        "memory": monitor.memory_usage(),
        "disks": monitor.disk_usage(),
        "uptime": monitor.uptime_total()
    }

if __name__ == "__main__":
    try:
        with Live(console=console, refresh_per_second=1) as live:
            while True:
                stats = gather_stats()
                live.update(Group(*ui.render_dashboard(stats)))
                time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n[bold red]Exiting System Monitor...[/bold red]")
