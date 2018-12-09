# Left Center Right
An automated implementation of a simple dice game.

## What is it?
[Left Center Right](https://en.wikipedia.org/wiki/LCR_(dice_game) "Wikipedia link") is a simple game of chance, with a simple set of rules:
* Each player starts with three tokens.
* On their turn, a player rolls up to three dice (one die per token, max three dice).  If a player has no tokens, they are skipped.
* The dice are labeled with "Left", "Center", and "Right" on three of the sides, and dots or circles on the remaining three sides.
* For each "Left" rolled, the player passes a token to the player on their left.
* For each "Right" rolled, the player passes a token to the player on their right.
* For each "Center" rolled, the player discards a token into the center of the table.
* A circle or dot means no action is taken.
* Play proceeds around the table until only one player has any tokens remaining.

As there are no decisions made, this game seemed easy to automate.  So I did!
