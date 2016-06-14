% Chinese Restaurant Process (CRP)
% Ref: Edwin Chen's Ruby code
%
% Author : Xi Tan (tan19@purdue.edu)
% Date   : 2/2/2015 (6/25/2014)
%
% Input:
%     - n     : Number of customers.
%     - alpha : Dispersion parameter. Smaller alpha encourages fewer clusters, larger alpha encourages more clusters.
% Output:
%     - table_assignments: A vector consists of table assignaments. The ith entry indicates the table assigned to the ith customer.

function table_assignments = CRP(n, alpha)
    table_assignments = zeros(1,n);
    next_empty_table = 1;
    
    for i = 1:n
        if(rand < alpha / (alpha + i - 1))
            % the ith customer chooses to sit on a new table.
            % Prob = alpha/(alpha+i-1)
            
            table_assignments(i) = next_empty_table;
            next_empty_table = next_empty_table + 1;
        else
            % the ith customer sits with one of the i-1 existing customers with equal probability.
            % Seen by the conditional probability. Prob = [n_k/(i-1)] * [1-alpha/(alpha+i-1)]
            
            table_assignments(i) = table_assignments(randi(i-1));
        end;
    end;       
end
