import pandas as pd
  
df = pd.read_excel(r"C:\Users\colle\Desktop\Pandas Tutorial\Customer Call List.xlsx")
df

df = df.drop_duplicates()
df

# removing not needed columns
df = df.drop(columns = "Not_Useful_Column")
df

# cleaning data in Last_Name column: lstrip(), rstrip(), strip() [only strips from outside of word] 
# default strip() only removes white space from left and right sides of word

# df["Last_Name"] = df["Last_Name"].str.lstrip("...") 
# df["Last_Name"] = df["Last_Name"].str.rstrip("_") 
# df["Last_Name"] = df["Last_Name"].str.rstrip("/") 
                    # OR
df["Last_Name"] = df["Last_Name"].str.strip("._/")
df

# all phone numbers need to have format xxx-xxx-xxxx
df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]', '', regex=True ) # return any char except a-z, A-Z, or 0-9, replace with ''
df

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x)) # make column string
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10]) # creates format xxx-xxx-xxxx
df

df["Phone_Number"] = df["Phone_Number"].str.replace('nan--', '')
df["Phone_Number"] = df["Phone_Number"].str.replace('Na--', '')
df

# change address column into 3 separate columns
df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',', n=2, expand=True) # creating the columns
df

# fix yes, no, Y, N = all Y, N
df["Paying Customer"] = df["Paying Customer"].str.replace('Yes', 'Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('No', 'N')

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes', 'Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No', 'N')
df

df = df.replace("N/a", "") # all columns
df = df.replace('NaN', '')
df = df.fillna('') # fix actual null columns to nothing
df

# give them a list of phone numbers they can call >> only show available people 
for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == "Y":
        df.drop(x, inplace=True)
        
df

for x in df.index:
    if df.loc[x, "Phone_Number"] == "":
        df.drop(x, inplace=True)
        
df
# another way to drop null values 
#df = df.dropna(subset="Phone_Number"), inplace=True

# reset index and drops original index
df = df.reset_index(drop=True)
df




