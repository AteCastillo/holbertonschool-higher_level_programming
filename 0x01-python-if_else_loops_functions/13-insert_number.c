#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - check the code for Holberton School students.
 * @head: doble pointer
 * @number: int received
 * Return: Always 0.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head;
	listint_t *newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
		return (NULL);

	newnode->n = number;

	if (tmp == NULL || tmp->n >= number) /*to add head or if head->n is
					      greater than number*/
	{
		newnode->next = tmp->next;
		tmp = newnode;
		return (newnode);
	}

	while (tmp != NULL)
	{
		if (tmp->next == NULL)
		{
			return (add_nodeint_end(head, number)); /*head because
						    it give a doble pointer*/
		}
		if (number <= tmp->next->n)
		{
			newnode->next = tmp->next;
			tmp->next = newnode;
			return (newnode);
		}
		tmp = tmp->next;
	}
	return(NULL);
}
