class Solution:
    def intToRoman(self, num: int) -> str:
        arr={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        s=''
        while num>=1000:
            s=s+'M'
            num-=1000
        while num>=900:
            s=s+"CM"
            num-=900
        while num>=500:
            s=s+"D"
            num-=500
        while num>=400:
            s=s+"CD"
            num-=400
        while num>=100:
            s=s+"C"
            num-=100
        while num>=90:
            s+="XC"
            num-=90
        while num>=50:
            s=s+"L"
            num-=50
        while num>=40:
            s+="XL"
            num-=40
        while num>=10:
            s=s+"X"
            num-=10
        while num>=9:
            s=s+"IX"
            num-=9
        while num>=5:
            s=s+"V"
            num-=5
        while num>=4:
            s+="IV"
            num-=num
        while num>=1:
            s=s+"I"
            num-=1
        return s

