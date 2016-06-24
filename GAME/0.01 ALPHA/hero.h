#include "main.h"

/*********************************************************************************
 * FUNCTION PROTOTYPES, MOVE THESE TO A "main.h" or similar if possible
 *********************************************************************************/
 
/* Function that will ask the user for his name and return this information to main */
void getName (void);

/* Function to init the players stats */
void playerStatGen (void);

/* Function to init the players gear */
void initPlayerGear (void);

/* Function to view players current inventory / weared gear */
void inventory (void);

/* Function to print out players current stats */
void heroStats (void);

#define AR_MULTIPLIER // Used for calculating damage (see hero.c player.dmg calculation)



/************************************************************************
 * HERO STATS 
 ************************************************************************/
	typedef struct {
		
		// PRIMARY STATS
		int 		level; // make sure there is an exp system added
		long long int 	exp;
		
		// SECONDARY STATS
		int 			ar;
	    	int 			dmg;
		/************************************************************************
		* BASE STATS - MODIFIED THROUGH LEVELS OR NAME CHANGE @ CHUCH
		************************************************************************/
		int 			base_def;
		int 			base_hp;
		int 			base_mp;
		int 			base_luck;
		int 			base_atk ;	// baseline attack, have equipped weapon ADD to this somehow but make sure that value is subtracted if weapon is removed 	
	    	char *			name;
	    
	    /************************************************************************
		* GEAR STAT TOTALS - TO BE ADDED TO BASE FOR ADJUSTED PLAYER VALUE 
		************************************************************************/
		int				bonus_def;
		int				bonus_hp;
		int				bonus_mp;
		int				bonus_luck;
		int				bonus_atk;
		int				resists	 ; //etc to add resist stats. 
		
		/************************************************************************
		* TOTAL STATS; BASE + GEAR - TO USE ON LIVE CHARACTER
		************************************************************************/
		int 			total_def;
		int 			total_hp;
		int 			total_mp;
		int 			total_luck;
		int 			total_atk ;
	   
	    
		// inventory stuff
		int				gold;
		// Figure out how to make a LIMITED SIZE inventory, i guess based on weight or total number of items.
		

		
	} NPC; // struct name

	// define a player of type NPC (above struct). This way we can reference it from multiple functions below.
	NPC player; // this is you

/***************************************************************************
 * It's an RPG right? Armor needs stats!!!  
 ***************************************************************************/
 
	typedef struct {
		char * itemName;
		char * itemType; 	// item type will be things like "Boots" or "Helm" and you'll need to make sure they can only occupy their matching slot in the gear struct.
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
		int hp;
		int luck; // increase to luck
		int exp;  // increase % of exp gain
		
		// bs for showcasing
		int l9aura;	// some kind of faggitaim aura. just for fun.
		int l10aura;
	} gear;
	
	

/******************************************************************************
 * Gear being worn by the player 
 ******************************************************************************/

	typedef struct {
		gear lefthand;
		gear righthand;
		gear shield; // The player can either use a weapon (dual wield) or a shield in right hand) BUT NOT BOTH
		gear chest;
		gear legs;
		gear hands;
		gear belt;
		gear head;
		gear ring0;
		gear ring1;
		gear neck;
	} wearing;
	
	wearing playerGear;
	





