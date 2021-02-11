#include "palindrome.h"

/**
 * is_palindrome - Check if is palindrome
 * @n: unsigned integer
 * Return: 1 if is Palindrome and 0 if no is Palindrome
 */
int is_palindrome(unsigned long n)
{
	unsigned long digits = 0;
    unsigned long sup = n;

	while (sup != 0)
	{
		digits *= 10;
		digits += (sup % 10);
		sup /= 10;
	}

	if (digits != n)
    {
		return(0);
    }
	return(1);
}
