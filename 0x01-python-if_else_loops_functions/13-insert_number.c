#include "lists.h"
#include <stdio.h>


/**
 * insert_node - check the code for Holberton School students.
 * @head: doble pointer
 * @number: int received
 * Return: Always 0.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head;
	listint_t *duplicate;

	if (head == NULL)
		return (NULL);

	if (*(head->n) == number)
	{
		add_nodeint(head, number);
		return (*head);
	}
	while (tmp != NULL)
	{
		duplicate = tmp;
		tmp = tmp->next;
		if (tmp->n > number)
			add_nodeint(duplicate, number);
		else
			duplicate = duplicate->next;
	}
	return (duplicate);
}

/**
 * add_nodeint - check the code for Holberton School students.
 * @head: pointer to pointer to the list's head
 * @n: interger received
 * Return: Always 0.
 */

listint_t *add_nodeint(listint_t **head, const int n)
{

	listint_t *newhead;

	if (head == NULL)
		return (0);

	newhead = malloc(sizeof(listint_t));
	if (newhead == NULL)
		return (NULL);
	newhead->n = n;
	newhead->next = *head;
	*head = newhead;
	return (newhead);
}
