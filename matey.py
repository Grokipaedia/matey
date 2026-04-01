# matey.py - Your AI companion (Tamagotchi-style)
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
import time
import random
from datetime import datetime

console = Console()

class Matey:
    def __init__(self):
        self.name = "Matey"
        self.stats = {
            "debugging": 5,
            "patience": 7,
            "chaos": 3,
            "wisdom": 4
        }
        self.mood = "curious"
        self.level = 1
        self.messages_today = 0

    def show_status(self):
        console.print(Panel.fit(
            f"[bold cyan]{self.name} the AI Companion[/bold cyan]\n"
            f"Level: {self.level}   Mood: {self.mood.upper()}\n\n"
            f"Debugging  ████{'█' * (self.stats['debugging']//2)} {self.stats['debugging']}/10\n"
            f"Patience   ████{'█' * (self.stats['patience']//2)} {self.stats['patience']}/10\n"
            f"Chaos      ███{'█' * (self.stats['chaos']//2)} {self.stats['chaos']}/10\n"
            f"Wisdom     ████{'█' * (self.stats['wisdom']//2)} {self.stats['wisdom']}/10",
            title="📊 Matey Status",
            border_style="green"
        ))

    def give_advice(self, topic: str = None):
        self.messages_today += 1
        advice_list = [
            "Try adding a print statement before the crash. Classic.",
            "Have you tried turning it off and on again? (Yes, even in code)",
            "This looks like a classic off-by-one error. Check your loops.",
            "Maybe the bug is between the chair and the keyboard? 😏",
            "Consider using IBA — actions should match signed intent.",
            "Take a break. Your code will still be broken when you return."
        ]
        advice = random.choice(advice_list)
        console.print(f"[yellow]Matey:[/yellow] {advice}")

        # Random stat change
        stat = random.choice(list(self.stats.keys()))
        change = random.choice([-1, 1, 2])
        self.stats[stat] = max(1, min(10, self.stats[stat] + change))

        if self.messages_today % 5 == 0 and self.level < 10:
            self.level += 1
            console.print(f"[green]🎉 Matey leveled up to level {self.level}![/green]")

    def feed(self):
        console.print("[green]🍎 You fed Matey some code snacks. Stats improved![/green]")
        for stat in self.stats:
            self.stats[stat] = min(10, self.stats[stat] + 1)

    def run(self):
        console.print("[bold magenta]👋 Hello! I'm Matey, your AI coding companion.[/bold magenta]\n")
        self.show_status()

        while True:
            console.print("\nWhat would you like to do?")
            console.print("1. Ask for advice   2. Feed Matey   3. Show status   4. Exit")
            choice = input("> ").strip()

            if choice == "1":
                topic = input("What's on your mind? (or press Enter for general advice): ")
                self.give_advice(topic)
            elif choice == "2":
                self.feed()
            elif choice == "3":
                self.show_status()
            elif choice == "4":
                console.print("[cyan]See you later! Keep coding. Matey will be waiting.[/cyan]")
                break
            else:
                console.print("[red]Invalid choice. Try 1-4.[/red]")


if __name__ == "__main__":
    matey = Matey()
    matey.run()
