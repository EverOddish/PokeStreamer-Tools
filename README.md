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
 6. Edit the first line of `auto_layout_gen4_gen5.lua` file from this repository with your favourite text editor and set `game` to the appropriate value, as described in the file
 7. Copy `auto_layout_gen4_gen5.lua` to the same directory that contains your sprite image files.
      * The script expects sprite files to be named as follows: `<pokemon_name>.png` (for example, `pikachu.png`)
      * The script expects party slot image files (that are monitored by OBS) to be named as follows: `p<slot_number>.png` (for example, `p1.png`)
      * The script expects a Pokeball image to be named `000.png`
 8. Copy `auto_layout_gen4_gen5_tables.lua` to the same directory
 9. Open Desmume and your Pokemon ROM, and load your save file
 10. In Desmume, open Tools > Lua Scripting > New Lua Script Window...
 11. Click Browse... and locate `auto_layout_gen4_gen5.lua` on your computer, open it, and click Run
 12. You should now be able to switch party slots, deposit/withdraw Pokemon from the PC, and catch Pokemon to see your party images update automatically!
 13. The Lua script output window should display all slot changes in text form.

### PKMN-NTR Setup

 1. Install custom firmware (CFW) on your 3DS: https://3ds.guide/
      * This process can take up to 2 hours, so be sure you have spare time
 2. Install BootNTR Selector on your 3DS: https://gbatemp.net/threads/release-bootntr-selector.432911/
 3. Install and run PKMN-NTR: https://github.com/drgoku282/PKMN-NTR/wiki
 4. Click on Tools > Event Handler
 5. Edit the event actions with a command specific to the directories on your computer, such as:
      * `del C:\\Users\\username\\sprites\\p###SLOT###.png & copy /Y C:\\Users\\username\\sprites\\###NAME###.png C:\\Users\\username\\sprites\\p###SLOT###.png & copy /b C:\\Users\\username\\sprites\\p###SLOT###.png+,, C:\\Users\\username\\sprites\\p###SLOT###.png`
 6. Click Apply and close the window
 7. Go back to the Read/Write tab, enter the IP address of your 3DS and click Connect
 8. Click Start Polling to start monitoring party data
 9. You should now be able to switch party slots, deposit/withdraw Pokemon from the PC, and catch Pokemon to see your party images update automatically!

### FAQ

 * Where can I find Pokemon sprite files?
     * https://veekun.com/dex/downloads
     * http://pkmn.net/?action=content&page=viewpage&id=8644
     * https://www.pkparaiso.com/xy/sprites_pokemon.php
 * What about Gen 1 and Gen 2 games?
     * These games are not supported yet
 * What about Pokemon in the PC boxes?
     * These are not supported yet
 * Why am I seeing strange behaviour? (missing Pokemon, fast switching, not updating properly)
     * Reading game memory directly is not always perfect. Try switching party members around, to see if the issue is corrected
 * What if I'm on an operating system whose emulator does not support Lua scripting? (for example, Desmume on Linux)
     * I'm sorry, you'll have to ask the maintainers of that emulator!
 * What if my question isn't answered here?
     * Tweet [@EverOddish](https://twitter.com/everoddish)

### Credits

 * A huge thank you to FractalFusion and MKDasher of Pokemon Speed Runs for their initial Lua script work! http://forums.pokemonspeedruns.com/viewtopic.php?t=314
 * A huge thank you to the 3DS modding community for their work on CFW, BootNTR, PKMN-NTR and others!
 * A huge thank you to PokemonChallenges for helping me test all this! (Check him out at http://twitch.tv/PokemonChallenges)
