# PokeStreamer-Tools
A set of scripts and tools for Pokemon streamers

## Automatic Layout Updating

If you're streaming a Pokemon game and like to display your current party on your layout, it can be tedious to modify which image files are displayed, while you are live. I've modified several existing tools to detect when in-game party slots change, which can then copy sprite image files on your computer automatically. Your streaming software can be configured to watch these files for modification, and update the layout accordingly. There is now also a "Soul Link" version that will update paired sprites at the same time.

## Dr. Fuji Twitch Extension

If you would like to use the Dr. Fuji Twitch Extension to display your Pokemon real-time stats on your stream, you can use the appropriate script to send live data to the server that will be displayed to users. Currently, this is only supported for the Gen 4/5 script.

## SOS Counter Tool

If you're doing SOS chains in Sun/Moon or Ultra Sun/Ultra Moon, this tool will display the current chain length. It will also write the value to a text file that can be monitored by streaming software and displayed on stream layouts. Note: This requires a version of Citra that supports Python scripting.

### Requirements

 * Windows operating system
 * An emulator with Lua scripting support
     * VBA-RR (for Gen 3 games)
     * Desmume (for Gen 4/Gen 5 games)

### VBA-RR Setup

 1. Download the latest release of VBA-RR: https://github.com/TASVideos/vba-rerecording/releases
 2. Edit the first line of `auto_layout_gen3.lua` file from this repository with your favourite text editor (you can right-click the file and Open With > Notepad): Set `game=1` to 1 for Ruby/Sapphire, 2 for Emerald, 3 for FireRed/LeafGreen
 3. Copy `auto_layout_gen3.lua` to the same directory that contains your sprite image files.
      * The script expects sprite files to be named as follows: `<pokemon_name>.png` (for example, `pikachu.png`)
      * The script expects party slot image files (that are monitored by OBS) to be named as follows: `p<slot_number>.png` (for example, `p1.png`)
      * The script expects a Pokeball image to be named `000.png`
 4. Copy `auto_layout_gen3_tables.lua` to the same directory
      * Note: The `auto_layout_gen3_tables.lua` file still needs to exist in the same directory, but you do not need to open it in VBA-RR
 5. Open VBA-RR and your Pokemon ROM, and load your save file
 6. In VBA-RR, open Tools > Lua Scripting > New Lua Script Window...
 7. Click Browse... and locate `auto_layout_gen3.lua` on your computer, open it, and click Run
 8. You should now be able to switch party slots, deposit/withdraw Pokemon from the PC, and catch Pokemon to see your party images update automatically!
 9. The Lua script output window should display all slot changes in text form. As a bonus, you can press "Q" to see Pokemon EV/IV values in your party

### Desmume Setup

 1. Download the latest release of Desmume: http://desmume.org/download/
 2. Make note of whether you downloaded 32-bit (x86) or 64-bit (x86-64) Desmume
 3. Download the Lua DLL that matches your Desmume: https://sourceforge.net/projects/luabinaries/files/5.1.5/Windows%20Libraries/Dynamic/
      * `lua-5.1.5_Win32_dll14_lib.zip` for x86 Desmume
      * `lua-5.1.5_Win64_dll14_lib.zip` for x86-64 Desmume
 4. Extract `lua5.1.dll` from the .zip file to the same folder where your `DeSmuME_0.9.11_x86.exe` or `DeSmuME_0.9.11_x64.exe` is
 5. Rename `lua5.1.dll` to `lua51.dll`
 6. Copy the correct script to the same directory that contains your sprite image files
      * `auto_layout_gen4_gen5_tables.lua` for regular automatic layout update
      * `auto_layout_gen4_gen5_tables_soul_link.lua` for Soul Link automatic layout update (paired sprites)
      * `auto_layout_gen4_gen5_tables_drfuji.lua` for sending data to the server for the Dr. Fuji Twitch Extension
      * The script expects sprite files to be named as follows: `<pokemon_name>.png` (for example, `pikachu.png`)
      * The script expects party slot image files (that are monitored by OBS) to be named as follows: `p<slot_number>.png` (for example, `p1.png`)
      * The script expects a Pokeball image to be named `000.png`
      * The Soul Link version of the script expects `soul_links.txt` containing which Pokemon are linked (see example file)
 7. Edit the first line of the chosen `.lua` file from this repository with your favourite text editor (you can right-click the file and Open With > Notepad) and set `game` to the appropriate value, as described in the file
      * If using the Dr. Fuji script, also set `username` to your Twitch username
 8. Open Desmume and your Pokemon ROM, and load your save file
 9. In Desmume, open Tools > Lua Scripting > New Lua Script Window...
 10. Click Browse... and locate `auto_layout_gen4_gen5.lua` (or other chosen version of the script) on your computer, open it, and click Run
      * Note: The `auto_layout_gen4_gen5_tables.lua` file still needs to exist in the same directory, but you do not need to open it in Desmume
 11. You should now be able to switch party slots, deposit/withdraw Pokemon from the PC, and catch Pokemon to see your party images update automatically!
 12. The Lua script output window should display all slot changes in text form.

### FAQ

 * Where can I find Pokemon sprite files?
     * https://drive.google.com/file/d/0Bx5dwDibVv9PNlJkWC0yajFrRms/view
     * https://drive.google.com/file/d/0Bx5dwDibVv9PX0dTOC1vU2xKdXc/view
     * https://veekun.com/dex/downloads
     * http://pkmn.net/?action=content&page=viewpage&id=8644
     * https://www.pkparaiso.com/xy/sprites_pokemon.php
 * What about Gen 1 and Gen 2 games?
     * These games are not supported
 * What about Pokemon in the PC boxes?
     * These are not supported
 * Why am I seeing strange behaviour? (missing Pokemon, fast switching, not updating properly)
     * Reading game memory directly is not always perfect. Try switching party members around, to see if the issue is corrected
 * What if I'm on an operating system whose emulator does not support Lua scripting? (for example, Desmume on Linux)
     * I'm sorry, you'll have to ask the maintainers of that emulator!
 * Do these scripts work with ROM hacks, such as Drayano's Storm Silver, etc.?
     * Yes!
 * Do these work on fan-made games?
     * No!
 * What if my question isn't answered here?
     * Tweet [@EverOddish](https://twitter.com/everoddish)

### Credits

 * A huge thank you to FractalFusion and MKDasher of Pokemon Speed Runs for their initial Lua script work! http://forums.pokemonspeedruns.com/viewtopic.php?t=314
 * A huge thank you to PokemonChallenges for helping me test all this! (Check him out at http://twitch.tv/PokemonChallenges)
 * A huge thank you to the contributors at https://projectpokemon.org for their reverse engineering of Pokemon games
