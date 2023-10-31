#include "lists.h"

/**
 * insert_node - inserts head
 * @head: head of the linked list.
 * @number: value to be inserted.
 *
 * Return: addres
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tp;
	listint_t *new;

	if (!head)
		return (NULL);
	if (!(*head))
		return (start_end(head, number, 10));
	if (number < (*head)->n)
	{
		new = start_end(head, number, 0);
		return (new);
	}
	tp = *head;
	while (tp->next)
	{
		if (number <= tp->next->n)
			break;
		tp = tp->next;
	}
	if (!tp)
		return (NULL);

	if (tp->next == NULL)
	{
		new = start_end(&tp, number, 1);
		return (new);
	}

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = tp->next;
	tp->next = new;
	return (new);
}

/**
 * start_end - handle end.
 * @head: head of list.
 * @num: the data.
 * @idx: flag.
 *
 * Return: new node.
*/
listint_t *start_end(listint_t **head, int num, int idx)
{
	listint_t *new;

	if (idx == 0)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);
		new->n = num;
		new->next = *head;
		*head = new;
		return (new);
	}
	else if (idx == 1)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);
		new->n = num;
		new->next = NULL;
		(*head)->next = new;
		return (new);
	}
	else
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);
		new->n = num;
		new->next = NULL;
		*head = new;
		return (new);
	}
}
