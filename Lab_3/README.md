# Lab 3
# Теоритическая база
Зачастую требуется быстро классифицировать объект на фотографии, не создавая сложных архитектур и не обучая заново всю сеть. В таком случае, очень помогают предобученные сети. 
В данной лабораторной работе будут продемонстрированы 3 свёрточных нейронных сети, каждая из них будет дообучена, после чего, будут рассчитаны интересующие нас метрики.
## Набор изображений
Текущий набор разбит на две выборки:
 * Train;
 * Valid.
 
Каждая из которых содержит в себе 10 различных классов:
1. Apples__Canker;
2. Apples__Monilia;
3. Apples__Powdery mildew;
4. Apples__Сedar rust;
5. Corn__Eyespot;
6. Corn__Northern leaf blight;
7. Corn__Southern rust;
8. Tomatoes__Gray rot;
9. Tomatoes__Late blight;
10. Tomatoes__Leaf mold.
![6](https://user-images.githubusercontent.com/82668230/205057629-c4a4c0f1-af1b-4e70-b334-0a6184a42a20.jpg)

# AlexNet
О сети:



Параметры обучения:
  ```
num_features = 9216
model.classifier = nn.Linear(num_features, 10)
if use_gpu:
    model = model.cuda()

loss_fn = nn.CrossEntropyLoss()

optimizer_ft = optim.Adam(model.parameters(), lr=1e-4)

exp_lr_scheduler = lr_scheduler.StepLR(optimizer_ft, step_size=7, gamma=0.1)
```
  ```
model, losses = train_model(model, loss_fn, optimizer_ft, exp_lr_scheduler, num_epochs=25)
```


