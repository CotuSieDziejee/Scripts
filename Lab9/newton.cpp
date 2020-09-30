#include <iostream>
#include <cmath>
#include <cfloat>
#include <cstdlib>

using namespace std;


double newton(unsigned n, double x, double eps, double epsF,
	      double (*F) (double), double (*P) (double)) {
			
  for (unsigned i = 0; i < n; ++i) {
    double dx = F(x)/P(x);
    x -= dx;
    if (fabs(dx) < eps || fabs(F(x)) < epsF) {
      break;
    }
  }
  return x;
}

inline double funkcja(double x) {
  return sqrt(x) - 2.0;
}

inline double pochodna(double x) {
  return 1.0/(2.0*sqrt(x));
}


int main(int argc, char* argv[]) {
  if (argc > 2) {
    unsigned int iteracje = atoi(argv[1]);
    double start = atof(argv[2]);
    double wynik = newton(iteracje, start, 1.0e-6, 1.0e-5, funkcja, pochodna);
    cout << "Rezultat: " << wynik << endl;
  } else {
    cerr << "./program maks_liczba_iteracji punkt_startowy\n";
  }
  return 0;
}
