#include "lists.h"

/**
 * check_pali - check palindrom.
 * @head: list.
 * @len: lenght.
 * Return: 0 or 1.
*/
int check_pali(listint_t *head, int len)
{
	listint_t *tp, *nums, *next_tp;
	int i, half, st_check = 0;

	half = len / 2, i = 0, tp = head, nums = NULL;
	while (tp)
	{
		if (i < half && !st_check)
		{
			next_tp = tp->next;
			tp->next = nums;
			nums = tp;
			tp = next_tp;
			i++;
		}
		if (i == half)
		{
			st_check = 1;
			if (len % 2 != 0)
				tp = tp->next;
			i--;
		}
		if (st_check)
		{
			if (nums->n != tp->n)
				return (0);
			nums = nums->next;
		}
		if (st_check)
			tp = tp->next;
	}
	return (1);
}

/**
 * is_palindrome - palindrom or not
 * @head: linked list head.
 *
 * Return: 0 or 1.
*/
int is_palindrome(listint_t **head)
{
	listint_t *tp, *pre = *head;
	int len = 0;

	if (!head)
		return (-1);
	else if (!(*head))
		return (1);
	else if (pre->next == NULL)
		return (1);

	tp = *head;
	while (tp)
	{
		tp = tp->next;
		len++;
	}

	return (check_pali(*head, len));
}

