#include "lists.h"

/**
 * insert_node - prints all elements of a listint_t list
 * @head: pointer to head of list
 * @number: pointer to head of list
 * Return: number of nodes
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *current = NULL;

	current = *head;

	/* creating the new node */
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (!*head)
	{
		*head = new_node;
		return (new_node);
	}

	/* node at the beginning */
	if (number < current->n)
	{
		new_node->next = (*head);
		*head = new_node;
		return (new_node);
	}

	/* node at the middle or end */
	while (current->next && (current->next->n < number))
		current = current->next;

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
