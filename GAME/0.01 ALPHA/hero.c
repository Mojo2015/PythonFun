/**********************************************************************************************************
 * Game/hero.c
 * Simple function to collect user information (name, )
 **********************************************************************************************************/

#include "main.h"
#include "hero.h"
#include "gear.h"

void playerStatGen (void);

	
/**********************************************************
 FUNCTION TO GET PLAYERS NAME
**********************************************************/

void getName (void)
{
	
	/* Variables */ 
	int x = 0; 								 // for the input loop below
	char * hero = malloc(sizeof(char) * 50); // player name will be stored here, free this at end of function

	/* ask for name */
	printf ("\n\nHola. What is your name?\n\n NAME: ");

	/* Loop to the maximum size of the player name, avoid stack overflow. */
	for (x; x < 50; x++) {
		hero[x] = getchar();
		if (hero[x] == '\n') {		// this WILL STORE the \n, so replace it below with NULL
			//fflush(stdin);			// dump any text the user entered that's not being stored now I don't believe this works for input, output only.
			break;
		}
	}
	
	printf ("\n\n");
	hero[x] = '\0';					// replace the newline \n with a string terminating NULL

	
	/* Temporary Welcome screen */
	printf ("Hello %s. Will you be the hero of the north? The savior of the fallen realms?\nDo you have what it takes to lead \
the norse to victory?\nOr will we succumb to the unending wrath of the tyrannical juden?\n", hero);

	/* Insert players name into the player struct (see hero.h) and free the memory occupied by the pointer (no longer needed) */
	player.name = hero;	
	//free (hero); // we shouldn't need that memory anymore, actually we do because player.name is a pointer. Freeing this throws it away.
	
}

/*********************************************************************************
 * FUNCTION TO INITIALIZE THE PLAYERS STATS 
 *********************************************************************************/
void playerStatGen (void)
{
	
	/* XXX: FOR NOW, WE NEED TO RUN THE playerStatGen(); function OVER AGAIN if you expect the stats to be updated to reflect gear. Things need to be initialized in a loop in a game.
	 * Not to mention if the user unequips or equips new gear, we need the stats to reflect it IMMEDIATELY */
	/* Since the struct is globally defined in the hero.h header, we can simply adjust them now with no function i/o */
	
	/* We're going to need BASE values and "BONUS" values (the value of the BASE + BOOST from gear. Because we need to be able to alter base values with levels too. */
	
	// PRIMARY STATS
	player.level = 1;
	player.exp   = 0;

	// SECONDARY STATS
	player.ar    = player.base_atk * 100;	// attack rating, used to generate chance to hit
	player.dmg	 = (float) player.base_atk * AR_MULTIPLIER + playerGear.righthand.damage;	// calculate player damage
	
	/************************************************************************
	* BASE STATS - MODIFIED THROUGH LEVELS OR NAME CHANGE @ CHUCH
	************************************************************************/
	player.base_def  = 5;
	player.base_hp   =18;
	player.base_mp   = 0;
	player.base_luck = 0;
	player.base_atk  = 5;
	
	// OTHER 
	player.gold  = 100;	// set inital gold to 100
	
	
	
	/************************************************************************
	* GEAR STAT TOTALS - TO BE ADDED TO BASE FOR ADJUSTED PLAYER VALUE 
	************************************************************************/
	
	// BONUS DEFENSE, add all armor defense modifiers together:
	player.bonus_def = playerGear.belt.defense
					 + playerGear.chest.defense
					 + playerGear.hands.defense
					 + playerGear.head.defense
					 + playerGear.lefthand.defense
					 + playerGear.legs.defense
					 + playerGear.neck.defense
					 + playerGear.righthand.defense
					 + playerGear.ring0.defense
					 + playerGear.ring1.defense;
					 
					 
	player.bonus_hp  = playerGear.belt.hp
					 + playerGear.chest.hp
					 + playerGear.hands.defense
					 + playerGear.head.defense
					 + playerGear.lefthand.defense
					 + playerGear.legs.defense
					 + playerGear.neck.defense
					 + playerGear.righthand.defense
					 + playerGear.ring0.defense
					 + playerGear.ring1.defense;	 
					 
	player.bonus_mp  = playerGear.belt.mp
					 + playerGear.chest.mp
					 + playerGear.hands.mp
					 + playerGear.head.mp
					 + playerGear.lefthand.mp
					 + playerGear.legs.mp
					 + playerGear.neck.mp
					 + playerGear.righthand.mp
					 + playerGear.ring0.mp
					 + playerGear.ring1.mp;
					 
	player.bonus_luck  = playerGear.belt.luck
					   + playerGear.chest.luck
					   + playerGear.hands.luck
					   + playerGear.head.luck
					   + playerGear.lefthand.luck
					   + playerGear.legs.luck
					   + playerGear.neck.luck
					   + playerGear.righthand.luck
					   + playerGear.ring0.luck
					   + playerGear.ring1.luck;
	
	/* THIS SHOULD BE REPLACED AS ATTACK IS A BASE STAT, GEAR SHOULD ONLY HAVE DAMAGE / AR				 
	player.bonus_atk = playerGear.belt.atk
					 + playerGear.chest.atk
					 + playerGear.hands.atk
					 + playerGear.head.atk
					 + playerGear.lefthand.atk
					 + playerGear.legs.atk
					 + playerGear.neck.atk
					 + playerGear.righthand.atk
					 + playerGear.ring0.atk
					 + playerGear.ring1.atk;			*/	 
	
	
	
	/************************************************************************
	* TOTAL STATS; BASE + GEAR - TO USE ON LIVE CHARACTER
	************************************************************************/
	player.total_def	= player.base_def  + player.bonus_def;
	player.total_hp		= player.base_hp   + player.bonus_hp;
	player.total_mp		= player.base_mp   + player.bonus_mp;
	player.total_luck	= player.base_luck + player.bonus_luck;
	//player.total_atk 	=;
	
	
	//player.name = hero;

	
	initPlayerGear(); // will probably move this but this is running the below function to actually put on my gear.
 
	
}

/*********************************************************************************
 * FUNCTION TO INITIALIZE THE PLAYERS STARTING GEAR
 *********************************************************************************/
void initPlayerGear (void)
{
	// run the gameGear function once to initialize all of the games armor types. Not sure how efficient this is. Later we should export that to a text
	// document and query it. This could be a huge waste of memory.

	gameGear();
	
	
	/* EQUIP THE PLAYERS STARTING GEAR */
	playerGear.righthand = short_sword;
	playerGear.chest     = nood;	// CURRENTLY_EQUIPPED.chest etc, this way we can pass it to other functions and it updates accordingly
	playerGear.ring0     = nood;
	playerGear.ring1	 = nood;
	playerGear.belt      = nood;
	playerGear.lefthand  = nood;
	playerGear.shield    = hoz;
	playerGear.legs      = nood;
	playerGear.head		 = nood;
	// For testing purposes, within another function, try to print out shit about my chest armor now.
}

/*********************************************************************************
 * FUNCTION TO VIEW AND EXAMINE USER EQUIPPED GEAR
 *********************************************************************************/

void inventory (void)
{
	
	int uinput; 	// for user input
	int loop = 1;   // bool value for loop below
	gear SELECTED;  // will be use for outputting the item stats to the user
	
	//TODO: HAVE EVERY ITEM TYPE AND ORGANIZE THEM BETTER (see ring0 and ring1 in stupid position)
	while (loop)
	{
		
	/* DISPLAY ITEMS PLAYER IS WEARING */
	printf ("You are currently wearing: \n");
	printf ("1. Chest     	: %s\n", playerGear.chest.itemName);
	printf ("2. Ring0     	: %s\n", playerGear.ring0.itemName);
	printf ("3. Belt      	: %s\n", playerGear.belt.itemName);
	printf ("4. Main hand 	: %s\n", playerGear.righthand.itemName);
	printf ("5. Off hand  	: %s\n", playerGear.shield.itemName);
	printf ("6. Boots     	: %s\n", playerGear.legs.itemName);
	printf ("7. Helm      	: %s\n", playerGear.head.itemName);
	printf ("7. Ring1      	: %s\n", playerGear.ring1.itemName);
	
	
	/* HAVE USER CHOOSE NEXT OPTION */
	printf ("\nEnter a value to print the items stats or enter 9 to quit: ");
	scanf  ("%1i", &uinput);
	//fflush (stdin);
	
	
	/* Assign user choice to buffer struct SELECTED and print its stats */	
	switch (uinput) {
		case 1: 
			SELECTED = playerGear.chest;
			printItemStats(SELECTED);
			break;
		case 2: 
			SELECTED = playerGear.ring0;
			printItemStats(SELECTED);
			break;
		
		case 3:
			SELECTED = playerGear.belt;
			printItemStats(SELECTED);
			break;
			
		case 4: 
			SELECTED = playerGear.righthand;
			printItemStats(SELECTED);
			break;
			
		case 5: 
			SELECTED = playerGear.shield;
			printItemStats(SELECTED);
			break;
		
		case 6: 
			SELECTED = playerGear.legs;
			printItemStats(SELECTED);
			break;
			
		case 7:
			SELECTED = playerGear.head;
			printItemStats(SELECTED);
			break;
			
		case 8:
			SELECTED = playerGear.ring1;
			printItemStats(SELECTED);
			break;
			
		case 9:
			loop = 0;	// set boolean to false to end the loop and exit function
			break;
			
		default: 
			break;
		}
		
	// end while loop
	}
		
		/* To do this seriously we're going to need some type of idea. We want to loop through the structs for the selected item and print all non-zero values. 
		 * I would like to do it without extreme redundancy, so it's going to need a variable like SELECTEDITEM.itemName etc. */
			
}

/*********************************************************************************
 * FUNCTION TO PRINT PLAYERS CURRENT STATS
 *********************************************************************************/			
void heroStats (void)
{
	
	playerStatGen();	// Because the stats are generated before the equipment in this program, we need to re-initialize to get the bonus from equipment.
	printf ("*************************************************\n");
	printf ("		STATS FOR %s\n					  \n", player.name);
	printf ("*************************************************\n");
	printf ("\n\n"												 );
	
	printf ("LEVEL  :		%i\n", player.level);
	printf ("EXP    :		%lli\n\n", player.exp);
	printf ("DEF    :		%i\n", player.total_def);
	printf ("MAX HP :		%i\n", player.total_hp);
	printf ("MAX MP :		%i\n", player.total_mp);
	printf ("LUCK   :		%i\n", player.total_luck);
	
	
	printf ("\n BATTLE STATISTITCS \n");
	printf ("----------------------\n");
	
	printf ("ATK			: %i\n", player.base_atk);
	printf ("Attack Rating	: %i\n", player.ar);
	printf ("DAMAGE			: %i\n", player.dmg);
	
	//test
	printf ("ATK * 1.2 + weapon damage, short sword does 3 DMG, so this should be 9\n");
	printf ("WEAPON DAMAGE = %i\n", playerGear.righthand.damage);
	
	sleep(5);
	
	
	
	
	
}
			
			
		/*	
			
			player.level = 1;
	player.gold  = 100;	// set inital gold to 100
	player.def = 5;
	player.hp    =18;
	player.mp    = 0;
	player.luck  = 0;
	player.atk   = 5;
	
	//secondary stats
	player.ar    = player.atk * 100;
	player.dmg	 = player.atk * 1.2 + playerGear.righthand.damage;
	//player.name = hero;
			
			
			
			
			*/ 
			
			
			
			
			
			
			
	
	

 
	
