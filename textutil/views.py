from django.http import  HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse("hello")
# def about(request):
#     return HttpResponse("about hello")




def index(request):

    return render(request,'index.html')

def analyzed(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'default')
    fullcaps = request.POST.get('fullcaps', 'default')
    spaceremover = request.POST.get('spaceremover', 'default')
    newlineremover = request.POST.get('newlineremover', 'default')
    charcounter = request.POST.get('charcounter', 'default')
    removenumber = request.POST.get('removenumber', 'default')
    removealpha = request.POST.get('removealpha', 'default')
    strr=djtext
    purpose=[]


    print(removepunc)
    print(djtext)
    if removepunc=="on":
        punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze=""
        for char in djtext:
            if char not in punctuation:
                analyze=analyze+char


        b=[]
        a = "Remove Punctuation. "
        purpose.append(a)


        params={'purpose':''.join(purpose),'analyzed_text':analyze}
        # return  render(request,'analyze.html',params)
        djtext=analyze
    if (fullcaps=="on"):
        analyze=""
        for char in djtext:
            analyze=analyze+char.upper()
        b = []
        a = "ALL CAPITAL. "
        purpose.append(a)

        params = {'purpose': ''.join(purpose), 'analyzed_text': analyze}
        # return render(request, 'analyze.html', params)
        djtext = analyze
    if (newlineremover=="on"):
        analyze=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyze=analyze+char
            else:
                print("no")
        print("pre",analyze)
        a = "New Line Remover. "
        purpose.append(a)

        params = {'purpose': ''.join(purpose), 'analyzed_text': analyze}
        # return render(request, 'analyze.html', params)
        djtext = analyze
    if (spaceremover=="on"):
        analyze=""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):

                analyze=analyze+char
        a = "Extraspace Remover. "
        purpose.append(a)

        params = {'purpose': ''.join(purpose), 'analyzed_text': analyze}
        # return render(request, 'analyze.html', params)
        djtext = analyze
    if (charcounter=="on"):
        analyze=""
        for char in djtext:
            if char in djtext:

                analyze= len(djtext)
        b=f"this is your text {djtext} and this is your countercharacter{analyze}"
        a = "Char Counter. "
        purpose.append(a)

        params = {'purpose': ''.join(purpose), 'analyzed_text': b}
        # params = {'purpose': purpose, 'analyzed_text': a}
        # return render(request, 'analyze.html', params)

    if removenumber == "on":
        number = '''0123456789'''
        # alpabet = '''abcdefghijklmnopqrstuvwxyz'''
        analyze = " "
        for index,char in enumerate(djtext):

            if not (djtext[index] == " " and djtext[index + 1] == " ") and char not in number:
                analyze = analyze + char
                print(analyze,end=" ")
            # if char not in alpabet:
            #     analyze = analyze + char

        b = []
        a = "Remove Number. "
        purpose.append(a)

        params = {'purpose': ''.join(purpose), 'analyzed_text': analyze}
        djtext = analyze
        # return  render(request,'analyze.html',params)
    if removealpha=="on":
        alpabet = '''abcdefghijklmnopqrstuvwxyz'''+'''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
        analyze=""
        for char in djtext:
            if char not in alpabet:
                analyze=analyze+char
                if "," in alpabet:
                    analyze = analyze + char
        sa=[]
        sa.append(analyze)
        print(sa)
        pun = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''
        sp=analyze.replace(",","\n")
        print(sp)



        b=[]
        a = "Remove Number "
        purpose.append(a)



        params={'purpose':''.join(purpose),'analyzed_text':sp}
        # return  render(request,'analyze.html',params)


    # if(removepunc !="on" or fullcaps !="on" or newlineremover !="on" or spaceremover !="on" or charcounter !="on"):
    #     return HttpResponse("Please select the Operation")

    return render(request, 'analyze.html', params)

