#include <unistd.h>
void print_alphabet(void)
{
	int	a;

	a = 'a';
	while (a <= 'z')
	{
		write(1, &a, 1);
		a++;
	}
}

int main(){
	print_alphabet();
	return 0;
}