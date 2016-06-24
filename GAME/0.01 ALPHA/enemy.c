/**********************************************************************************************************
 * Game/enemy.c
 * This is the file that will be used to generate enemies and their attributes
 **********************************************************************************************************/

#include "main.h"
#include "enemy.h"
#include "battle.h"


enemy enemies (void)
{
	enemy beta_phaggot, Undeadhamed, FaggiTaimFrankie, GeileyPoop, DonDiggie;
	
	beta_phaggot.level = 1;
	beta_phaggot.name = malloc(sizeof(char) * 50);
	beta_phaggot.name = "Beta Phaggot";
	beta_phaggot.hp = 10;
	beta_phaggot.def = 2; 	

	DonDiggie.level = 1;
	DonDiggie.name = malloc(sizeof(char) * 50 );
	DonDiggie.name = "Don Diggie";
	DonDiggie.hp = 6;
	DonDiggie.def = 2;

	/* REPLACE WITH RNG */
	int dothis;	

	

	printf ("What enemy do you want to face? Enter a number\n");
	scanf ("%i", &dothis);
	fflush(stdin);

	// Will need to store the enemy name into another varibale
	enemy CURRENT;

	switch (dothis)
	{
		case 0:
			CURRENT = beta_phaggot;
			break;
		case 1: CURRENT = DonDiggie;
			break;
		default:
			printf ("Bad Choice FGT");
			//exit(1);
	}			 
			


/**********************************************************************************************************************************************/
// CONTINUED:
	
	printf ("You chose to battle a %s\n", CURRENT.name);		
	battle(CURRENT);
}




