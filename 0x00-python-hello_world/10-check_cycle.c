#include "lists.h"

/**
 * check_cycle - check for loop.
 * @list: linked list.
 *
 * Return: 0.
*/
int check_cycle(listint_t *list)
{
	listint_t *flash = list;
	listint_t *snail = list;

	while (flash && flash->next)
	{
		flash = flash->next->next;
		snail = snail->next;

		if (flash == snail)
			return (1);
	}
	return (0);
}
