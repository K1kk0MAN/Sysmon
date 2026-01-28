from rich.panel import Panel
from rich.table import Table
from rich.console import Group
from rich.progress import Progress, BarColumn, TextColumn, ProgressColumn
from utils import bytes_format

def usage_bar_row(label: str, used: str, total: str, percent: float, color: str = "green"):
    progress = Progress(
        TextColumn("{task.percentage:>5.1f}%", justify="right"),
        BarColumn(bar_width=40, complete_style=color),
        expand=False,
        transient=True,
    )
    task = progress.add_task("", total=100, completed=percent)

    return (label, f"{used} / {total}", progress)

def render_dashboard(stats):
    
    cpu_table = Table.grid(padding=(0, 1))
    for i, usage in enumerate(stats["cpu"]):
        label = f"Core {i}"
        cpu_table.add_row(*usage_bar_row(label, "", "", usage, color="cyan" if usage < 75 else "red"))
    Panel(cpu_table, title="CPU Usage")
    
    ram = stats["memory"]
    ram_table = Table.grid(padding=(0, 1))
    ram_table.add_row(*usage_bar_row("RAM", bytes_format(ram["used"]), bytes_format(ram["total"]), ram["percent"], color="magenta" if ram["percent"] < 75 else "red"))

    ram_panel = Panel(ram_table, title="Memory Usage")

    disk_table = Table.grid(padding=(0, 1))
    for d in stats["disks"]:
        color = "yellow" if d["percent"] < 80 else "red"
        disk_table.add_row(*usage_bar_row(d["name"], bytes_format(d["used"]), bytes_format(d["total"]), d["percent"], color))

    disk_panel = Panel(disk_table, title="Disk Usage")

    return [
        Panel(cpu_table, title="CPU Usage"),
        ram_panel,
        disk_panel,
        Panel(f"[bold]Uptime:[/bold] {stats['uptime']}", title="System Uptime"),
    ]