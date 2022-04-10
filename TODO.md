# Game updates

## Goal for this update
- Basic ship map (bridge, engine room, quarters, lounge, cargo bay)
- Dinosaurs randomly dropped around ship
- Food randomly dropped around ship
- Machines in different rooms
- Have dinosaurs walk from room to room (random walk)
- If hungry: eat food (if available)
- If not hungry: talk with other dinosaurs or use machines
- Dinosaurs sleep when tired

### 1. Locations
1. Make a map representation. Rooms (nodes) with exits (edges).
   - Are rooms or exits entities? Or maybe available_exits is a part of the location component.

### 2. Entities
1. Update dinosaur spawner, make one that randomly places dinosaurs around ship.
2. Create food entity (one-time or multi-use?)
3. Create machine entity

### 3. Creature Simulation
1. Add satiety and energy to components
2. Add starvation
3. Add tiredness

### 4. Creature Behaviors
1. Walk/move
2. Eat (food)
3. Sleep
4. Talk (to dinosaur)
5. Use (machine)

### 5. Creature AI
1. Move randomly
2. Eat when hungry
3. Sleep when tired
4. Otherwise, talk/use
