#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
#include <cstdlib>

using namespace std;

int main() {
    string file, id;
    string s, a;
    int k = 0;
    string **mas = NULL;
    int i = 1;
    cout << "Enter the file path" << endl;
    cin >> file;
    cout << "Enter the id" << endl;
    cin >> id;
    ifstream f(file);
    if (!f.is_open()) {
        cout << "Error" << endl;
        return 2;
    }
    while (!f.eof()) {
        getline(f, s);
        if (k == 0)
            a = s;
        k++;
    }
    int p = 0;
    p = a.find(',');
    while (p != -1) {
        i++;
        p = a.find(',', p + 1);
    }
    mas = new string *[k];
    for (int j = 0; j < k; j++)
        mas[j] = new string[i];
    f.clear();
    f.seekg(0, ios_base::beg);
    p = 0;
    while (!f.eof()) {
        getline(f, s);
        p++;
        unsigned long o = 0;
        mas[p - 1][i - 1] = s.substr(s.rfind(',') + 1);
        for (int j = 0; j < i - 1; j++) {
            mas[p - 1][j] = s.substr(o, s.find(',', o) - o);
            o = s.find(',', o) + 1;
        }
    }
    int origin=-1, dest=-1, duration=-1, sms=-1;
    for (int j=0; j<i; j++){
    }
    for (int j=0; j<i; j++){
        if(mas[0][j].compare("msisdn_origin")==0)
            origin = j;
        if(mas[0][j].compare("msisdn_dest")==0)
            dest = j;
        if(mas[0][j].compare("call_duration")==0)
            duration = j;
        if(mas[0][j].compare("sms_number")==0)
            sms = j;
    }
    double origin_call=0, dest_call=0, sms_summ=0, summ=0;
    for (int j=0;j<k; j++){
        for (int r = 0; r < i; r++)
            if(mas[j][r]==id){
                if (r==origin)
                    origin_call+=3*(double)stod(mas[j][duration]);
                if (r==dest)
                    dest_call+=1*(double)stod(mas[j][duration]);
                sms_summ+=1*(double)stod(mas[j][sms]);
            }
    }
    summ=origin_call+dest_call+sms_summ;
    cout<<origin_call<<" Rub for outgoing calls"<<endl;
    cout<<dest_call<<" Rub for incoming calls"<<endl;
    cout<<sms_summ<<" Rub for SMS"<<endl;
    cout<<summ<<" Rub for all"<<endl;
    return 0;
}
