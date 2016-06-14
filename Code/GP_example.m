function GP_example()
%
% To be updated.
%

a = -10;
b = 10;
n = 10;
pn = 100;

x = a+(b-a)*rand(n,1);
f = sin(x);
x_predict = linspace(a, b+1, pn);

f_predict = cv(x_predict,x)*inv(cv(x,x))*f; % mean of prediction
v_predict = cv(x_predict,x_predict)-cv(x_predict,x)*inv(cv(x,x))*cv(x,x_predict); % variance of prediction

hold on;
plot(x,f,'+black','LineWidth',5);
plot(x_predict,f_predict+2*diag(v_predict),'-.blue','LineWidth',1);
plot(x_predict,f_predict,'-red','LineWidth',2);
plot(x_predict,f_predict-2*diag(v_predict),'-.blue','LineWidth',1);
end


function K = cv(x,y)
    for i = 1:length(x)
        for j = 1:length(y)
            K(i,j) = exp(-0.5*(x(i)-y(j))^2);
        end;
    end;
end

