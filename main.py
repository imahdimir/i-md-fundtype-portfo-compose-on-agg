"""

    """

import json

from githubdata import GithubData


class GDU :
    with open('gdu.json') as f :
        gj = json.load(f)

    src = gj['src']
    slf = gj['slf']

gu = GDU()

class ColName :
    jm = 'JMonth'
    ft = 'FundType'
    stck = 'Stocks & Preffered Shares'
    fxi = 'Fixed Income'
    depo = 'Deposits'
    cash = 'Cash'
    othr = 'Others'

c = ColName()

class OrgColName :
    ft = 'نوع صندوق'
    stck = 'سهام و حق تقدم سهام'
    fxi = 'اوراق بهادار با درآمد ثابت'
    depo = 'گواهی سپرده و سپرده بانکی'
    cash = 'نقد'
    othr = 'سایر'

oc = OrgColName()

def main() :
    pass

    ##
    gd = GithubData(gu.src)
    gd.overwriting_clone()
    ##
    df = gd.read_data()
    ##
    ren = {
            oc.ft   : c.ft ,
            oc.stck : c.stck ,
            oc.fxi  : c.fxi ,
            oc.depo : c.depo ,
            oc.cash : c.cash ,
            oc.othr : c.othr ,
            }
    df = df.rename(columns = ren)
    ##
    df[c.jm] = df[c.jm].astype('string')
    df[c.jm] = df[c.jm].str[0 :4] + '-' + df[c.jm].str[4 :6]
    ##
    ord = {
            c.ft   : None ,
            c.jm   : None ,
            c.stck : None ,
            c.fxi  : None ,
            c.depo : None ,
            c.cash : None ,
            c.othr : None ,
            }

    df = df[ord.keys()]
    ##
    df.to_excel(gd.data_fp , index = False)
    ##
    msg = 'cols renamed by: '
    msg += gu.slf
    ##
    gd.commit_and_push(msg)

    ##

    gd.rmdir()

    ##

##
if __name__ == "__main__" :
    main()
    print('Done!')
