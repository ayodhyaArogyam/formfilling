from django.shortcuts import render,redirect,get_object_or_404
from .models import FormfillingUser,Referralform

# Create your views here.


def formfilling(request):
    if request.method == 'POST':



        member = request.POST.get('member')
        if member == None:
            return render(request,'formstage1.html',{'active': True})
        else:
            return redirect('stage2')
        # print(member)
    return render(request,'formstage1.html',{})

def formstage2(request):

    if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            who_invited = request.POST.get('Who_invited')
            date_visit = request.POST.get('date_visit')
            hear_about = request.POST.get('hear_about')

            company_name = request.POST.get('company_name')
            Your_industry = request.POST.get('Your_industry')
            professional_classifiction = request.POST.get('professional_classifiction')
            Address1 = request.POST.get('Address1')
            Address2 = request.POST.get('Address2')
            city = request.POST.get('city')
            state = request.POST.get('state')
            postal = request.POST.get('postal')
            email = request.POST.get('email')
            website = request.POST.get('website')
            number1 = request.POST.get('number1')
            number2 = request.POST.get('number2')
            gst = request.POST.get('gst')
            experience = request.POST.get('experience')
            edu_background = request.POST.get('edu_background')
            revoke_license = request.POST.get('revoke_license')
            primary_occupation = request.POST.get('primary_occupation')
            commitment = request.POST.get('commitment')
            qualified_substitue = request.POST.get('qualified_substitue')
            bring_referral = request.POST.get('bring_referral')
            quantity_referral = request.POST.get('quantity_referral')
            bkmember = request.POST.get('bkmember')
            otherOrg = request.POST.get('otherOrg')
            ref_firs_name = request.POST.get('ref_first_name')
            ref_last_name = request.POST.get('ref_last_name')
            ref_bussiness_name = request.POST.get('ref_bussiness_name')
            ref_phone = request.POST.get('ref_phone')
            ref_email = request.POST.get('ref_email')
            ref_business_rel1 = request.POST.get('ref_business_rel1')
            ref_business_rel2 = request.POST.get('ref_business_rel2')
            ref_firs_name2= request.POST.get('ref_first_name2')
            ref_last_name2 = request.POST.get('ref_last_name2')
            ref_bussiness_name2 = request.POST.get('ref_bussiness_name2')
            ref_phone2 = request.POST.get('ref_phone2')
            ref_email2 = request.POST.get('ref_email2')
            print(date_visit)

            try:
                 
                form = FormfillingUser(first_name=first_name,last_name=last_name,who_invited=who_invited,
                                    date_visit=date_visit,company_name=company_name,Your_industry=Your_industry,
                                    professional_classifiction=professional_classifiction,Address1=Address1,Address2=Address2,
                                    city=city,state=state,postal=postal,email=email,website=website,number1=number1,number2=number2,
                                    gst=gst,experience=experience,edu_background=edu_background,revoke_license=revoke_license,
                                    primary_occupation=primary_occupation,commitment=commitment,qualified_substitue=qualified_substitue,
                                    bring_referral= bring_referral,quantity_referral=quantity_referral,bkmember=bkmember,
                                    otherOrg=otherOrg,hear_about=hear_about)
                form.save()
                print('formsave')

                refferaldata = Referralform(ref_firs_name =ref_firs_name,ref_last_name=ref_last_name,ref_email=ref_email,
                                            ref_phone=ref_phone,ref_business_rel1=ref_business_rel1,formuser=form )
                refferaldata.save()
                print('refferal save')
                if(ref_email2):
                        
                        refferaldata2 = Referralform(ref_firs_name =ref_firs_name2,ref_last_name=ref_last_name2,ref_email=ref_email2,
                                            ref_phone=ref_phone2,ref_business_rel1=ref_business_rel2, formuser=form )
                        refferaldata2.save()
                return render(request,'formstage2.html',{'message':'Successfull Sent'})

            except Exception as e:
                 print(e)
                 return render(request,'formstage2.html',{'message':'something went worng in creating '})
            

            


    return render(request,'formstage2.html',{})



def listformuser(request):
     try:
          user =FormfillingUser.objects.all().prefetch_related('referralform_set')
     except:
          return render(request,'listformfillup.html',{'message': 'Someting Went worng....'}) 

     return render(request,'listformfillup.html',{'user': user})



def singleformuser(request,pk):
     user = get_object_or_404(FormfillingUser, pk=pk)
     print(user)
     return render(request,'singleformuser.html',{'u':user})