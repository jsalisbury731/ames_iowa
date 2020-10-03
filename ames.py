import pandas as pd
import numpy as np

def rename(df):
    df_rename = df.rename(columns = {'Id':'Id',
                                     'Lot Area':'lot_area',
                                     'Street':'street',
                                     'Land Contour':'land_cont',
                                     'Neighborhood':'neighborhood',
                                     'Condition 1':'cond_1',
                                     'Condition 2':'cond_2',
                                     'Bldg Type':'bldg_type',
                                     'House Style':'style',
                                     'Overall Cond':'overall_cond',
                                     'Year Built':'yr_built',
                                     'Year Remod/Add':'yr_remodeled',
                                     'Roof Style':'roof_style',
                                     'Exter Cond':'exter_cond',
                                     'Foundation':'foundation',
                                     'Bsmt Cond':'bsmt_cond',
                                     'BsmtFin Type 1':'bsmt_fin_1',
                                     'BsmtFin Type 2':'bsmt_fin_2',
                                     'Total Bsmt SF':'bsmt_sf',
                                     'Heating':'heat',
                                     'Central Air':'cent_air',
                                     'Gr Liv Area':'gr_liv_area',
                                     'Full Bath':'full_bath',
                                     'Half Bath':'half_bath',
                                     'Bedroom AbvGr':'bedrooms_gr',
                                     'Kitchen AbvGr':'kitchen',
                                     'Kitchen Qual':'kitch_qual',
                                     'Fireplaces':'fireplaces',
                                     'Garage Type':'garage_type',
                                     'Garage Cars':'garage_car_size',
                                     'Paved Drive':'paved_drive',
                                     'Pool QC':'pool_qual',
                                     'Yr Sold':'year_sold'
                                     })
    included_cols = ['Id',
                     'lot_area',
                     'street',   # Secondary, removing from first model, value split of 2044 / 7
                     'land_cont',   # Value split of 1843 / 85 / 80 / 43
                     'neighborhood',
                     'cond_1',
                     'cond_2',  # Secondary, removing from first model, value split of 2025 (Normal) / 26 (other values)
                     'bldg_type',
                     'style',
                     'overall_cond',   # Secondary variable to investigate
                     'yr_built',
                     'yr_remodeled',
                     'roof_style',   # Secondary variable to investigate
                     'exter_cond',
                     'foundation',   # Secondary variable to investigate
                     'bsmt_cond',   # Secondary, removing from first model, 1834 (Typicals) / 92 (Good | Excellent) / 70 (Fair | Poor)
                     'bsmt_fin_1',   # Secondary variable to investigate
                     'bsmt_fin_2',   # Secondary variable to investigate
                     'bsmt_sf',
                     'heat',   # Secondary, removing from first model, value split of 2018 (GasA) / 33 (other values)
                     'cent_air',   # Secondary variable to investigate
                     'gr_liv_area',
                     'full_bath',
                     'half_bath',
                     'bedrooms_gr',
                     'kitchen',   # Secondary variable to investigate
                     'kitch_qual',
                     'fireplaces',   # Secondary variable to investigate
                     'garage_type',
                     'garage_car_size',
                     'paved_drive',   # Secondary, removing from first model, 1861 (Paved) / 39 (Partial) / 151 (Dirt/Gravel)
                     'pool_qual',   # Consider removing from first model, only 9 houses with pools
                     'year_sold'
                     ]

    if 'SalePrice' not in df.columns:
        df_rename = df_rename[included_cols]
    else:
        df_rename = df_rename[included_cols].merge(df[['Id', 'SalePrice']], left_on='Id', right_on='Id', how='left')
        df_rename = df_rename.rename(columns = {'SalePrice':'sale_price'})
    return df_rename

##########################################

def map(df):
    # Created has_pool column to use binary data if house has pool and disregard condition/quality
    df['has_pool'] = np.where(df['pool_qual'].isnull(), 0, 1)

    # Replace null values
    # https://www.geeksforgeeks.org/python-pandas-dataframe-fillna-to-replace-null-values-in-dataframe/
    df['bsmt_sf'] = df["bsmt_sf"].fillna(0)
    df["bsmt_cond"] = df["bsmt_cond"].fillna('None')
    df["bsmt_fin_1"] = df["bsmt_fin_1"].fillna('None')
    df["bsmt_fin_2"] = df["bsmt_fin_2"].fillna('None')
    df["garage_type"] = df["garage_type"].fillna('None')

    # Replace garage_car_size (NaN) with median value
    df["garage_car_size"] = df["garage_car_size"].fillna(df["garage_car_size"].median())

    # Drop the pool_qual column, already converted to has_pool
    df.drop(columns=['pool_qual'], inplace=True)

    # Enter cond_2 values of [RRNn, RRAn, RRNe, RRAe] for cond_1 values if cond_1 values [Artery, Feedr, Norm, PosN, or PosA]
    for num in range(len(df)):
        cond_tst_1a = df['cond_2'][num] == 'RRAn'
        cond_tst_1b = df['cond_2'][num] == 'RRAe'
        cond_tst_2a = df['cond_2'][num] == 'RRNn'
        cond_tst_2b = df['cond_2'][num] == 'RRNe'
        cond_tst_2c = df['cond_1'][num] != 'RRAn'
        cond_tst_2d = df['cond_1'][num] != 'RRAe'
        gets_replaced = df['cond_1'][num]
        does_replacing = df['cond_2'][num]
        if cond_tst_1a or cond_tst_1b:
            df.replace(gets_replaced, does_replacing, inplace=True)
        elif (cond_tst_2a or cond_tst_2b) and (cond_tst_2c or cond_tst_2d):
            df.replace(gets_replaced, does_replacing, inplace=True)

    # Mapping small neighborhoods to larger adjacent neighborhoods
    df['neighborhood'] = df['neighborhood'].map({'NAmes':'NAmes',
                                                 'CollgCr':'CollgCr',
                                                 'OldTown':'OldTown',
                                                 'Edwards':'Edwards',
                                                 'Somerst':'Somerst',
                                                 'NridgHt':'NridgHt',
                                                 'Gilbert':'Gilbert',
                                                 'Sawyer':'Sawyer',
                                                 'SawyerW':'SawyerW',
                                                 'Mitchel':'Mitchel',
                                                 'BrkSide':'BrkSide',
                                                 'Crawfor':'Crawfor',
                                                 'IDOTRR':'IDOTRR',
                                                 'Timber':'Timber',
                                                 'NoRidge':'NoRidge',
                                                 'StoneBr':'StoneBr',
                                                 'SWISU':'SWISU',
                                                 'ClearCr':'ClearCr',
                                                 'MeadowV':'MeadowV',
                                                 'Blmngtn':'Blmngtn',
                                                 'BrDale':'BrDale',
                                                 'Veenker':'Veenker',
                                                 'NPkVill':'NPkVill',
                                                 'Blueste':'Crawfor',
                                                 'Greens':'Somerst',
                                                 'GrnHill':'Timber',
                                                 'Landmrk':'Somerst'
                                                })

    # Mapping style to groups
    df['style'] = df['style'].map({'1Story':'1Story',
                                   '2Story':'2Story',
                                   '1.5Fin':'Fin',
                                   'SLvl':'SLvl',
                                   'SFoyer':'SFoyer',
                                   '2.5Unf':'Unfin',
                                   '1.5Unf':'Unfin',
                                   '2.5Fin':'Fin'
                                  })

    # Mapping overall_cond to combine three lowest values
    df['overall_cond'] = df['overall_cond'].map({1:3,
                                                 2:3,
                                                 3:3,
                                                 4:4,
                                                 5:5,
                                                 6:6,
                                                 7:7,
                                                 8:8,
                                                 9:9
                                                })

    # Mapping roof_style so small groups go to Other
    df['roof_style'] = df['roof_style'].map({'Gable':'Gable',
                                             'Hip':'Hip',
                                             'Flat':'Other',
                                             'Gambrel':'Other',
                                             'Mansard':'Other',
                                             'Shed':'Other'
                                            })

    # Mapping exter_cond to combine like categories
    df['exter_cond'] = df['exter_cond'].map({'TA':'TA',
                                             'Gd':'Gd',
                                             'Fa':'Fa',
                                             'Ex':'Gd',
                                             'Po':'Fa'
                                            })

    # Mapping foundation to combine smaller categories to Other
    df['foundation'] = df['foundation'].map({'PConc':'PConc',
                                             'CBlock':'CBlock',
                                             'BrkTil':'BrkTil',
                                             'Slab':'Other',
                                             'Stone':'Other',
                                             'Wood':'Other'
                                            })

    # Mapping exter_cond to combine like categories
    df['bsmt_cond'] = df['bsmt_cond'].map({'TA':'TA',
                                           'Gd':'Gd',
                                           'Fa':'Fa',
                                           'Ex':'Gd',
                                           'Po':'Fa',
                                           'None':'None'
                                            })

    # Mapping heating to group non-gas options
    df['heat'] = df['heat'].map({'GasA':'GasA',
                                 'GasW':'GasW',
                                 'Wall':'NonGas',
                                 'Grav':'NonGas',
                                 'OthW':'NonGas'
                                })

    # Mapping kitchen to groups
    df['kitchen'] = df['kitchen'].map({1:1,
                                       0:1,
                                       3:2,
                                       2:2
                                      })

    # Mapping fireplaces to groups
    df['fireplaces'] = df['fireplaces'].map({0:0,
                                             1:1,
                                             2:2,
                                             3:2,
                                             4:2
                                            })

    # Mapping garage_car_size to groups
    df['garage_car_size'] = df['garage_car_size'].map({0:0,
                                                       1:1,
                                                       2:2,
                                                       3:3,
                                                       4:3,
                                                       5:3
                                                      })

    # Mapping kitch_qual to combine like categories
    df['kitch_qual'] = df['kitch_qual'].map({'TA':'TA',
                                             'Gd':'Gd',
                                             'Fa':'Fa',
                                             'Ex':'Ex',
                                             'Po':'Fa',
                                            })

    # Mapping cond_1 to combine like categories
    df['cond_1'] = df['cond_1'].map({'Norm':'Norm',
                                     'Feedr':'Artery',
                                     'Artery':'Artery',
                                     'RRAn':'RRA',
                                     'PosN':'Fa',
                                     'PosA':'Fa',
                                     'RRAe':'RRA',
                                     'RRNn':'RRN',
                                     'RRNe':'RRN'
                                    })

    return df
