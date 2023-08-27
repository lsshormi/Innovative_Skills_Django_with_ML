# part 1

cake1 = "Black forest,"
cake2 = "Vanilla cake,"
cake3 = "Red Velvet,"
cake4 = "Lemon Sponge Cake,"
cake5 = "Chocolate Cake."

print("Each cake flavor types: ",cake1,cake2,cake3,cake4,cake5)

# part 2
# per pound inventory cost for each cake

raw_m_c1 = 180  # raw material cost
raw_m_c2 = 150
raw_m_c3 = 220
raw_m_c4 = 165
raw_m_c5 = 170

t_c = 150  # transportation cost for each pound

raw_m_c_t_c1 = raw_m_c1 + t_c 
raw_m_c_t_c2 = raw_m_c2 + t_c
raw_m_c_t_c3 = raw_m_c3 + t_c
raw_m_c_t_c4 = raw_m_c4 + t_c
raw_m_c_t_c5 = raw_m_c5 + t_c

# Add 3% utility cost on material and transportation cost in total for each pound
u_c = 3/100

u_c1 = raw_m_c_t_c1 + (raw_m_c_t_c1*u_c)
u_c2 = raw_m_c_t_c2 + (raw_m_c_t_c2*u_c)
u_c3 = raw_m_c_t_c3 + (raw_m_c_t_c3*u_c)
u_c4 = raw_m_c_t_c4 + (raw_m_c_t_c4*u_c)
u_c5 = raw_m_c_t_c5 + (raw_m_c_t_c5*u_c)

s_c = 50   # space cost
st_c = 60  # staff cost

# total inventory cost for Per pound each cake
total_i_c1 = u_c1 + s_c + st_c
total_i_c2 = u_c2 + s_c + st_c
total_i_c3 = u_c3 + s_c + st_c
total_i_c4 = u_c4 + s_c + st_c
total_i_c5 = u_c5 + s_c + st_c

print("Inventory cost for Per pound each cake: ",total_i_c1,total_i_c2,total_i_c3,total_i_c4,total_i_c5)

# part 3

# visualize each cake's per pound selling price before discount

selling_p_b_d_c1 = 780
selling_p_b_d_c2 = 600
selling_p_b_d_c3 = 800
selling_p_b_d_c4 = 650
selling_p_b_d_c5 = 660

print("Selling price per pound before discount: ",selling_p_b_d_c1,selling_p_b_d_c2,selling_p_b_d_c3,selling_p_b_d_c4,selling_p_b_d_c5)

# part 4

# visualize each cake's per pound selling price after discount
d1 = 5/100  # getting 5% discount
d2 = 7/100  # getting 7% discount

selling_p_a_d_c1 = selling_p_b_d_c1 - (selling_p_b_d_c1*d1)
selling_p_a_d_c2 = selling_p_b_d_c2 - (selling_p_b_d_c2*d1)
selling_p_a_d_c3 = selling_p_b_d_c3 - (selling_p_b_d_c3*d1)
selling_p_a_d_c4 = selling_p_b_d_c4 - (selling_p_b_d_c4*d2)
selling_p_a_d_c5 = selling_p_b_d_c5 - (selling_p_b_d_c5*d2)

print("Selling price per pound after discount: ",selling_p_a_d_c1,selling_p_a_d_c2,selling_p_a_d_c3,selling_p_a_d_c4,selling_p_a_d_c5)


# part 5
# sells how many pounds for each cake.

p_c1 = 5
p_c2 = 7
p_c3 = 10
p_c4 = 5
p_c5 = 9

# estimate total amount of profit after sell for each cake
# total profit = selling price × total_pound - inventory cost × total_pound

total_p_c1 = (selling_p_a_d_c1*p_c1) - (total_i_c1*p_c1)
total_p_c2 = (selling_p_a_d_c2*p_c2) - (total_i_c2*p_c2)
total_p_c3 = (selling_p_a_d_c3*p_c3) - (total_i_c3*p_c3)
total_p_c4 = (selling_p_a_d_c4*p_c4) - (total_i_c4*p_c4)
total_p_c5 = (selling_p_a_d_c5*p_c5) - (total_i_c5*p_c5)

print("Total profit after sell for each cake: ",total_p_c1,total_p_c2,total_p_c3,total_p_c4,total_p_c5)

# part 6
# estimate % of profit after sell for each cake
# Profit % = (selling price - inventory cost) / inventory cost * 100

profit_c1 = total_p_c1 / (total_i_c1*p_c1)*100
profit_c2 = total_p_c2 / (total_i_c2*p_c2)*100
profit_c3 = total_p_c3 / (total_i_c3*p_c3)*100
profit_c4 = total_p_c4 / (total_i_c4*p_c4)*100
profit_c5 = total_p_c5 / (total_i_c5*p_c5)*100

print("Estimate profit Percentage for each cake: ","{:.2f}".format(profit_c1),"{:.2f}".format(profit_c2),"{:.2f}".format(profit_c3),"{:.2f}".format(profit_c4),"{:.2f}".format(profit_c5))
