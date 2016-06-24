/* battle.c */


#include "main.h"
#include "enemy.h"
#include "hero.h"
#include "gear.h"

	// remember, its not a struct, we used typedef so it would be enemy, just so long as its in a referenced header file.
void battle (enemy CURRENT)
{
/************************************************************************************************************
 DEMO BATTLE, MOVE THIS TO ITS OWN SOURCE FILE, THIS IS PURELY FOR TESTING 
*************************************************************************************************************/

	int choice;
	//int herohp = 2;


	//printf ("\n ENCOUNTERED A %s!!!\n", CURRENT.name);

	//testing first
	printf ("Ok this is the battlefile\n, your name is %s\n, the enemy you're fighting is a %s\n", player.name, CURRENT.name);

	while (CURRENT.hp > 0) {

	// GET USER INPUT FOR USER TURN IN BATTLE /
		printf ("Please select an option:\n1: Attack\n2: Run\n3: Cry like a bitch\n");
		scanf ("%i", &choice);
		fflush(stdin);
		

	// add rand and seed srand to randomize the chances of hits, damage, etc
		switch (choice) {
			case 1:
				printf ("You hit the little fucker for 2 damage!\n");
				CURRENT.hp -= 2;
				break;
			case 2: 
				printf ("Trying to run away like a little fgt\n");
				// needs a % chance based on luck stat
				printf ("You succeeded, lucky little prick\n");
				break;
			case 3: 
				printf ("You proceed to cry like a little fgt, hopefully the %s leaves you alone\n", CURRENT.name);
				break;

			default:
				printf ("What a bullshit selection moron\n");
				continue;
		// close switch
		}
	

	sleep(2);
	
	
	if (CURRENT.hp) {
		printf ("%s attacked you! Hit you for 12 damage PUSSY\n", CURRENT.name);
		player.total_hp -= 12; }
	else
		printf ("The %s is dead, you ripped his fucking face apart bro\n", CURRENT.name);

	
	if (player.total_hp <= 0){
		printf ("YOU ARE DEAD, GAME OVER HAHAHAHAHA NOOB\n");
		break;
	}

	// close while
	}
	
}
