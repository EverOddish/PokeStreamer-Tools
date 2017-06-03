# PokeStreamer-Tools
A set of scripts and tools for Pokemon streamers

## Automatic Layout Updating

If you're streaming a Pokemon game and like to display your current party on your layout, it can be tedious to modify which image files are displayed, while you are live. I've modified several existing tools to detect when in-game party slots change, which can then copy sprite image files on your computer automatically. Your streaming software can be configured to watch these files for modification, and update the layout accordingly.

### Requirements

 * An emulator with Lua scripting support
     * VBA-RR (for Gen 3 games)
     * Desmume (for Gen 4/Gen 5 games)
 * A 3DS with custom firmware (CFW)
     * BootNTR and PKMN-NTR (for Gen 6/Gen 7 games)

### VBA-RR Setup

 1. Download the latest release of VBA-RR: https://github.com/TASVideos/vba-rerecording/releases
 2. Edit the first line of `auto_layout_gen3.lua` file from this repository with your favourite text editor: Set `game=1` to 1 for Ruby/Sapphire, 2 for Emerald, 3 for FireRed/LeafGreen
 3. Copy `auto_layout_gen3.lua` to the same directory that contains your sprite image files.
      * The script expects sprite files to be named as follows: `<pokemon_name>.png` (for example, `pikachu.png`)
      * The script expects party slot image files (that are monitored by OBS) to be named as follows: `p<slot_number>.png` (for example, `p1.png`)
      * The script expects a Pokeball image to be named `000.png`
 4. Copy `auto_layout_gen3_tables.lua` to the same directory
 5. In VBA-RR, open Tools > Lua Scripting > New Lua Script Window...
 6. Click Browse... and locate `auto_layout_gen3.lua` on your computer, open it, and click Run
 7. You should now be able to switch party slots, deposit/withdraw Pokemon from the PC, and catch Pokemon to see your party images update automatically!
 8. The Lua script output window should display all slot changes in text form. As a bonus, you can press "Q" to see Pokemon EV/IV values in your party

### Desmume Setup

### PKMN-NTR Setup

### FAQ

 * What about Gen 1 and Gen 2 games?
     * These games are not supported yet
 * What about Pokemon in the PC boxes?
     * These are not supported yet
 * Why am I seeing strange behaviour? (missing Pokemon, fast switching, not updating properly)
     * Reading game memory directly is not always perfect. Try switching party members around, to see if the issue is corrected

### Credits

 * A huge thank you to FractalFusion and MKDasher of Pokemon Speed Runs for their initial Lua script work! http://forums.pokemonspeedruns.com/viewtopic.php?t=314
 * A huge thank you to the 3DS modding community for their work on CFW, BootNTR, PKMN-NTR and others!
 * A huge thank you to PokemonChallenges for helping me test all this! (Check him out at http://twitch.tv/PokemonChallenges)
