/* This file will contain all of the usable gear in the game 
 * if it becomes too long, break it into separate functions for each type
 *  UNTIL I LEARN HOW TO DEAL WITH ALL THESE HEADERS WITHOUT ERRORS AND CONFLICTS
 *   MOVING THIS TO THE BOTTOM OF hero.h UNFORTUNATELY. */
 
 /* FIND OUT IF malloc() is necessary for all of this. Anything you allocate has to be freed so that will get tricky */
 /* OK THE ARMOR TYPES NEED TO BE DECLARED IN THE HEADER FILE PERIOD, BUT THE VALUES CAN BE INITIALIZED HERE. SO MOVE THINGS LIKE "armor soj;" to gear.h and this will work. */
 
 #include "main.h" // gear struct global variable is contained here. Do not remove.
 #include "hero.h"
 #include "gear.h" // all item names defined here
 
 /* This is a function that needs to actually be run if you expect these values to be defined */
void gameGear (void)
{
	
	/* REFERENCE SO YOU KNOW WHAT TO INCLUDE IN GEAR 
	 * typedef struct {
		char *itemName;
		char *itemType; 	// item type will be things like "Boots" or "Helm" and you'll need to make sure they can only occupy their matching slot in the gear struct.
		int damage;
		int defense;
			// resists
		int cold;
		int fire;
		int light;
		int psn; 
		int all; // all resists
		
			// other stats
		int ar;	// attack rating
		int vit; // increase to vitality
		int mp;  // increase to mana
		int luck; // increase to luck
		int exp;  // increase % of exp gain
	} armor, weapon; 
	*/ 
	
	/* Note, find some way to only init these items if the player is either carrying, has them equipped, or one drops. This is going to cause a major memory leak tbh. */
	
	
/*********************************************************************************
 *		EQUIPPABLE RINGS 
 *********************************************************************************/
	
		/* STONE OF JORDAN */
		soj.itemName = "Stone of Jerr-dan";
		soj.itemType = "Ring";
		soj.all = 10;
		soj.vit = 10;
		soj.luck = 5;
		soj.exp = 5;
		
		/* JoHameds FaggiTaim Band Ring */
		joh.itemName = "Johamed's Faggitaim Band Ring";
		joh.itemType = "Not Bul Katho's";
		joh.luck     = 69;
		joh.l9aura   = 50;	// chance to cast level 9 aura. this is just for fun.
		
		foa.itemName = "Heavenly Angus";
		foa.itemType = "Ring of Pure Beef";
		foa.l10aura  = 1;
		foa.vit = -76;
		
		
/*********************************************************************************
 *		EQUIPPABLE BELTS
 *********************************************************************************/
	
		/* LE CRACKED SASH */
		c_sash.itemName = "Le Cracked Sash";
		c_sash.itemType = "Belt";
		c_sash.defense  = 1;
		
/*********************************************************************************
 *		EQUIPPABLE CHEST ARMOR 
 *********************************************************************************/
	
		/* QUILTED VEST */
		//quilt.itemName = malloc(sizeof(char) * 50);
		quilt.itemName = "Quilted Vest";
		quilt.itemType = "Chest";
		quilt.defense  = 8;

		
		
/*********************************************************************************
 *  	EQUIPPABLE WEAPONS
 ********************************************************************************/
 
	/* SWORDS */
		//short_sword.itemName = malloc(15);
		short_sword.itemName = "Short Sword";
		short_sword.itemType = "Sword";
		short_sword.damage   = 3; 
		
/*********************************************************************************
 *  	EQUIPPABLE SHIELDS
 ********************************************************************************/
		
	/* TOWER SHIELDS */
		//hoz.itemName = malloc(25);
		hoz.itemName = "Herald of Zakapwn";
		hoz.itemType = "Shield";
		hoz.defense  = 10;
		hoz.damage   = 4; 	// only if its used to attack. DO NOT ADD THIS TO CHARS BASE
		hoz.all		 = 5;
		
		
/*********************************************************************************
 *  	EQUIPPABLE BOOTS
 ********************************************************************************/
		
	/* BASIC */
		leather_boots.itemName = "Leather Boots";
		leather_boots.itemType = "Boots";
		leather_boots.defense  = 2;
		
/*********************************************************************************
 * HELMS
 *********************************************************************************/
		leather_hat.itemName = "Leather Hat";
		leather_hat.itemType = "Helm";
		leather_hat.defense  = 2;
		










// printf ("All gear has been initialized\n"); was just using this to debug, remove if no longer necessary
}
		
		
		
/*********************************************************************************
 * FUNCTION TO PRINT ITEM STATS, MUST BE CALLED WITH AN EXISTING ITEM PASSED AS ARG
 *********************************************************************************/
void printItemStats(gear SELECTED)
{
	char buffer;
	printf ("\n\n");
	// ONLY PRINT OUT NON ZERO VALUES
	
	//All items have a name and item type, no if needed
		printf ("Item Name        : %s\n", SELECTED.itemName);
		printf ("Item Type        : %s\n", SELECTED.itemType);
	

		
/* Since items have many possible stats, we'll run through each here and only print the nonzero values
 * this will have the net effect of printing the exact stats physically added to each item, the rest of
 * the struct contents are already zero, so they will simply not be displayed 							*/
 	
	if (SELECTED.damage && SELECTED.itemType == "Sword") // BUG ALERT, OTHER WEAPONS BESIDES SWORDS WONT DISPLAY, UPDATE AS NEEDED.
		printf ("Damage           : %i\n", SELECTED.damage);
	
	else if (SELECTED.damage && SELECTED.itemType == "Shield")
		printf ("Smite Damage     : %i\n", SELECTED.damage);
		
	if (SELECTED.defense)
		printf ("Defense          : %i\n", SELECTED.defense);
	if (SELECTED.cold)
		printf ("Cold Resist      : +%i\n", SELECTED.cold);
	if (SELECTED.fire)
		printf ("Fire Resist      : +%i\n", SELECTED.fire);
	if (SELECTED.light)
		printf ("Lightning Resist : +%i\n", SELECTED.light);
		
	if (SELECTED.psn)
		printf ("Poison Resist    : +%i\n", SELECTED.psn);
		
	if (SELECTED.all)
		printf ("Resist All       : +%i\n", SELECTED.all);
		
	if (SELECTED.ar)
		printf ("Attack Rating    : +%i\n", SELECTED.ar);
		
	if (SELECTED.vit)
		printf ("Vitality         : +%i\n", SELECTED.vit);
		
	if (SELECTED.mp)
		printf ("Mana             : +%i\n", SELECTED.mp);
		
	if (SELECTED.luck)
		printf ("Luck             : +%i\n", SELECTED.luck);
	if (SELECTED.exp)
		printf ("Experience       : +%i%%\n", SELECTED.exp);
		
		// this stuff is just bs for screen shots. 
	if (SELECTED.l9aura)
		printf ("Level 9 Aura of The Homogai");
	if (SELECTED.l10aura)
		printf ("Level 20 Fist of Thine Agnus");
		
	//printf ("\npress enter to continue");
	//scanf  (" %c ", &buffer);

	printf ("\n\n");
	sleep(4);
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
