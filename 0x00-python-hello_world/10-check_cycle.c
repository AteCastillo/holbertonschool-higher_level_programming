#include "lists.h"
/**
 * check_cycle - check the code for Holberton School students.
 * @list: int received
 * Return: an int.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
	{
		return (0);
	}
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
