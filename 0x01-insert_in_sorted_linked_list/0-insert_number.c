#include "lists.h"

/**
 * insert_node - prints all elements of a listint_t list
 * @head: pointer to head of list
 * @number: pointer to head of list
 * Return: number of nodes
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newNode = malloc(sizeof(listint_t));
    listint_t *current;

    if (newNode == NULL)
        return(NULL);
    newNode->n = number;
    if (head == NULL)
    {
        newNode = add_nodeint_end(head, number);
        *head = newNode;
        return(newNode);
    }
    current = *head;
    if (current == NULL)
    {
        newNode->next = NULL;
        return(newNode);
    }
    if (current->n > number)
    {
        newNode->next = current;
        *head = newNode;
        return(newNode);
    }
    while (current->next->n < number && current->next->next != NULL)
    {
        current = current->next;
    }
    if (current->next != NULL)
    {
        current = current->next;
    }
    if (current->n < number)
    {
        add_nodeint_end(head, number);
    }
    else
    {
        newNode->next = current->next;
        current->next = newNode;
    }
    return(newNode);
}
