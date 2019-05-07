#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int e, n, d;
int* encrypt_result;
char* decrypt_result = "";
int length = 0;

int int_pow(num, round){
	int result=1;
	for (int i = 0; i < round; ++i)
	{
		result *= num;
	}
	return result;
}

int not_prime(int num){
	for (int i = 2; i <= sqrt(num); ++i){
		if (num % i == 0) return 1;
	}

	if(num == 0)
		return 1;
	else
		return 0;
}

int gcd ( int a, int b )
{
  int c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}

int mul_inverse(int e, int phi)
{
    int d = 0;
    int x1 = 0;
    int x2 = 1;
    int y1 = 1;
    int temp_phi = phi;
    
    while (e > 0){
        int temp1 = temp_phi/e;
        int temp2 = temp_phi - temp1 * e;
        temp_phi = e;
        e = temp2;
        
        int x = x2- temp1* x1;
        int y = d - temp1 * y1;
        
        x2 = x1;
        x1 = x;
        d = y1;
        y1 = y;  	
    }
    
    if (temp_phi == 1)
        return d + phi;
    return 0;
}

void encrypt(char* message){
	for (int i = 0; i < length; i++)
	{
		printf("%d\n", message[i]);
		printf("%f\n", pow(message[i], d));
		// int c = pow(message[i], d) % n;
		// printf("%d\n", c);
		// encrypt_result[i] = c;
	}
}

void decrypt(){
	for (int i = 0; i < length; i++)
	{
		printf("%d\n", int_pow(encrypt_result[i], e));
		char c = int_pow(encrypt_result[i], e) % n;
		decrypt_result += c;
	}
}

void gen_keypair(int p, int q){
	// printf("%d, %d\n", not_prime(p), not_prime(q));
	if(not_prime(p) || not_prime(q)){
		printf("%s\n", "Not prime");
	}
	if(p == q){
		printf("%s\n", "p and q shouldn't same");
	}

	int phi = (p - 1) * (q - 1);

	n = p * q;
	e = rand() % (phi - 1) + 2;

	while(gcd(e, phi) != 1){
		e = rand() % (phi - 1) + 2;
	}

	d = mul_inverse(e, phi);

}


int main(int argc, char const *argv[]){
	int p, q;

	printf("%s\n", "Input P value:");
	scanf("%d", &p);
	printf("%s\n", "Input Q value:");
	scanf("%d", &q);

	gen_keypair(p, q);

	printf("%d, %d, %d\n", e, d, n);

	char* message = "12";
	length = strlen(message);

	encrypt_result = ( int * )malloc(sizeof(int) * strlen(message));
	encrypt(message);
	// for (int i = 0; i < strlen(message); ++i)
	// {
	// 	printf("%d\n", encrypt_result[i]);
	// }
	decrypt();
	printf("%s\n", decrypt_result);

	return 0;
}