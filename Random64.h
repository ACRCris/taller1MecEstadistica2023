#include<iostream>
#include<cmath>
using namespace std;

//Constantes del generador aleatorio

class Crandom{
	unsigned long long u,v,w;
	
	public:
		Crandom(unsigned long long j);
		unsigned long long int64();
		double r() {return 5.42101086242752217E-20 * int64();} // pa que o que?
		unsigned int int32(){return (unsigned int) int64();};
		double exponencial(float tau);
		double gauss(float mu,float sigma);
		unsigned long long getu1();
		unsigned long long getv1();
		unsigned long long getw1();
		
};

Crandom::Crandom(unsigned long long j){
    v=4101842887655102017LL; w=1;
    u = j ^ v; // Operador XOR que se comporta como un OR exclusivo y tambien como la suma en los Planos finitos P2^n
	//cout<<"prin data1 "<<u<<" "<<v<<" "<<w<<endl;
	int64();
	//cout<<"prin data2 "<<u<<" "<<v<<" "<<w<<endl;
    v = u;
	//cout<<"prin data3 "<<u<<" "<<v<<" "<<w<<endl; 
	int64();
	//cout<<"prin data4 "<<u<<" "<<v<<" "<<w<<endl;
    w = v;
	//cout<<"prin data5 "<<u<<" "<<v<<" "<<w<<endl; 
	int64();
	//cout<<"prin data6 "<<u<<" "<<v<<" "<<w<<endl;

}
unsigned long long Crandom::int64() {
    u = u * 2862933555777941757LL + 7046029254386353087LL;
	//cout<<"data1 "<<u<<" "<<v<<" "<<w<<endl;
    v ^= v >> 17; 
	//cout<<"data2 "<<u<<" "<<v<<" "<<w<<endl;
	v ^= v << 31; 
	//cout<<"data3 "<<u<<" "<<v<<" "<<w<<endl;
	v ^= v >> 8;
	unsigned long long a = w>>32;
	//cout<<"data4 "<<u<<" "<<v<<" "<<w<<" "<<a<<endl;
    w = 4294957665U*(w & 0xffffffff) + (w >> 32);
	//cout<<"data5 "<<u<<" "<<v<<" "<<w<<endl;
    unsigned long long x = u ^ (u << 21); 
	//cout<<"data6 "<<u<<" "<<v<<" "<<w<<" "<<x<<endl;
	x ^= x >> 35; 
	//cout<<"data7 "<<u<<" "<<v<<" "<<w<<" "<<x<<endl;
	x ^= x << 4;
	//cout<<"data8 "<<u<<" "<<v<<" "<<w<<" "<<x<<endl;
	unsigned long long r = (x+v)^w;
	//cout<<"data9 "<<u<<" "<<v<<" "<<w<<" "<<x<<" "<<r<<endl;
    return (x + v) ^ w;
}

double Crandom::exponencial(float tau){
	return -tau*log(r());
}

double Crandom:: gauss(float mu,float sigma){
	return sigma*sqrt(-2*log(r()))*cos(2*M_PI*r())+mu;
}

unsigned long long Crandom:: getu1(){
	return u;
}

unsigned long long Crandom:: getv1(){
	return v;
}

unsigned long long Crandom:: getw1(){
	return w;
}
