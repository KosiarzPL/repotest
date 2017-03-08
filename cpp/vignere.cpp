/*
 * vignere.cpp
 *
 *
 *
 */


using namespace std;
#include <iostream>
#include <string>


int main(int argc, char **argv)
{
    //char tekst[120];
    string tekst, szyfrogram,odszyfrowany;
    cout <<"Podaj tekst do zaszyfrowania:";
    cin >>tekst;

    cout << tekst << endl << "Rozmiar" << tekst. size() << endl;
    szyfrogram.resize(tekst.size());
    for (unsigned int i = 0; i<tekst.size(); i++) {
        cout << tekst[i] << " ";
     szyfrogram[i] = zakodowany_znak;

    }

	return 0;
}

