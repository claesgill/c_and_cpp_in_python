#include <iostream>

extern "C" {
    void hello(void);
    int sum(int, int);
    unsigned int sumrange(int, int, int);
}

void hello(void){
    std::cout << "Hello from C++" << std::endl;
}

int sum(int a, int b){
    return a + b;
}

unsigned int sumrange(int a, int b, int range){
    int someting = 0;
    unsigned int total = 0;
    for(int x = 0; x < range; x++){
        for(int y = 0; y < range; y++){
            someting += x*x + x*y + y;
            total = x+y;
        }
    }
    return total;
}

int main(void){ return 0; }