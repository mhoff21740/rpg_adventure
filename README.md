Project Summary: RPG Adventure — A Python-Based Text RPG
    RPG Adventure is a fully interactive, dungeon-crawling text-based RPG developed in Python. This project was designed as a comprehensive capstone to reinforce concepts learned in both an Intro to Python course and an Object-Oriented Programming (OOP) course. The game showcases structured programming practices, modular design, and dynamic gameplay mechanics that reflect both foundational and intermediate Python skills.

Learning Objectives & Concepts Demonstrated
This project highlights my ability to design and implement a complete Python application using core programming concepts including:

Intro to Python Concepts

    Control flow: Conditional logic and loops govern exploration, combat, and player decisions.

    Functions: Modular helper functions simplify inventory management, combat sequences, and level-ups.

    Data structures: Lists, dictionaries, and tuples are used extensively to manage characters, items, rooms, inventory, and game logic.

    Randomization: The random module creates dynamic enemy spawns, loot drops, room generation, and encounter variety.

    Input handling: The game accepts player commands to drive turn-based progression.

Object-Oriented Programming (OOP)

    Abstraction: Core gameplay mechanics (e.g., attack behavior, loot, movement) are abstracted into class methods.

    Inheritance: Custom classes such as Wizard, Rogue, and Ranger inherit from a base character class, enabling polymorphic behavior.

    Polymorphism: Class-specific combat logic allows each player type to act differently in battle while sharing a common interface.

    Encapsulation (Optional): Game state and character stats are cleanly managed within class structures.

Gameplay Features
Player Characters

    Players can choose unique character classes with distinct combat styles and abilities.

    Players can fight each other or enemies, loot items, and manage inventory.

    On death, characters drop items which become available to others.

Procedural Dungeon & Room Logic

    Dungeons are randomly generated with every playthrough, including:

        Unique room descriptions

        NPC and player spawns

        Secrets, hidden mechanics, and items

        Dynamic exits and directional logic

        Visited room tracking

    Ranger class has a specialized looting system to ensure arrow pickups are battle-ready, whereas other characters store items passively.

    Conditional item interaction exists (e.g., a player without a fishing rod cannot catch a goldfish—it escapes).

Combat System

    Turn-based battles support class-specific strategies:

        Wizards gain new spells at higher levels.

        Rangers rely on arrow-based ranged attacks with fallback to melee.

        Each class has unique attack methods and resource management.

    NPCs and players can fight freely with dynamic targeting.

    Boss rooms introduce unique enemies and environmental modifiers that alter combat mechanics.

    Combat is responsive to player level, scaling enemy health and difficulty accordingly.

Leveling & Progression

    Experience points (XP) are gained from defeating NPCs and player characters.

    Characters follow a D&D-inspired stat progression system:

        Ability modifier increases on odd-numbered levels starting from level 3.

        Health and combat power increase with levels.

        Higher levels unlock advanced spells and combat techniques.

    NPCs drop less XP than player characters, adding a layer of strategy and progression pacing.

Technical Strengths & Scalability
    Modular file structure for combat, exploration, room logic, characters, and enemies.

    Easily expandable architecture for adding quests, new classes, inventory limits, save/load systems, or GUI enhancements.

    Strong code readability and extensibility thanks to clean function and class design.

Summary
This project served as a hands-on, end-to-end learning platform for reinforcing Python fundamentals and OOP design. It reflects my ability to:

    Design scalable systems with reusable class architecture

    Model real-world systems through data and logic abstraction

    Combine storytelling with functional programming principles

    Build maintainable, modular applications in Python