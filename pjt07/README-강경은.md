## 강경은_구현 내용

```
단계별로 구현 과정 중 학습한 내용, 어려웠던 부분,
새로 배운 것들 및 느낀 점 등을 상세히 기록하여 제출해야 합니다
```

```
@login_required
@require_http_methods(['GET','POST'])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance=request.user)

    context ={
        'form':form,
    }
    return render(request,'accounts/update.html',context)

```

decorators를 통해 로그인이 된 상태여야만 update기능을 사용할 수 있도록 구현하고,

커스텀 모델을 통해 변수를 정의하고 유효성 검사 및 render와 redirect를 구현하였다.



```
#forms.py
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email','first_name','last_name',)

```

from django.contrib.auth.forms 로 UserCreationForm과 UserChangeForm의 기능을 불러와

이를 통해 커스텀 모델을 구현하였다. 이를 위해서는 django.contrib.auth로 불러온 get_user_model()

으로 model을 정의해주어야 했다.



최종적으로 accounts의 기능은 전부 구현하였고, movies의 기능은 시간관계상 update의 기능까지

구현이 완료되었다.



### 강경은_어려웠던 부분

```
개인적으로는 커스텀 모델을 정의하고 활용하는 부분이 가장 어려웠다.
어느 모델에서는 어느 부분을 상속받고 이후 views.py에서 이를 활용하는 것에서 난관을 겪었다.
또한 from django에서 특정 경로를 찾아 거기에서 update_session_auth_hash나 
require_http_methods등의 기능들을 뽑아내는 것이 큰 어려움이었다.
```



### 강경은_느낀 점

```
첫 페어 프로그래밍이어서 굉장히 긴장이 되었다.
내가 발목을 잡지는 않을까 고민이 되어 혼자 진행할 사람은 미리 말을 하라고 하셨을 때 말할까
말까 굉장히 고민을 많이 했으나, 결국 피하기만 해서는 앞으로의 직정에서도 어려움이 많을 것이라
는 생각에 페어 프로그래밍을 진행하게 되었다.
같은 페어가 된 남은열 조원은 무척 활기차고 코딩 수준이 뛰어나, 옆에 있던 나까지 즐거워지는
활력이 느껴졌다. 덕분에 나도 몇 시간 동안 즐겁게 대화하며 코딩을 진행할 수 있어서 무척
고마웠다.
```

