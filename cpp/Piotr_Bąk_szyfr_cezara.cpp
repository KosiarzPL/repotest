#include <iostream>

using namespace std;

char lower15(char d) {
{
    return char((int)d+32);

}

void szyfruj(char tekst[], int klucz) {
    int i = 0; // indeks
    klucz = klucz % 26;
    while (tekst[i] != '\0') {

        if (tekst[i] == ' ')
            continue;

        if ((int)tekst[i] >=65 && (int)tekst[i] <=90)
            tekst[i] = lower15 (tekst[i]);
        if ((int)tekst[i] + klucz > 122)
            tekst[i] = (char)((int)tekst[i] + klucz - 26);
        else
            tekst[i] = (char)((int)tekst[i] + klucz);

        i++;
                                                            // (int)tekst[i] - rzutowanie na kod ascii
                                                            // (char)((int)tekst[i]) - zamiana kodu ascii na znak
    }
    cout << tekst;
}

int main(int argc, char **argv) {

    char tekst[100];
    int klucz = 3;
	cout << "Podaj tekst do zaszyfrowania" << endl;
	// cin >> tekst;
    cin.getline(tekst, 100);
    cout << "Podaj klucz";
    cin >> klucz;
    szyfruj(tekst, klucz);


    return 0;
}

