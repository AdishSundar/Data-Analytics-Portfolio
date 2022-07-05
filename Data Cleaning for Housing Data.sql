select *
from PortfolioProject.dbo.NashvilleHousing

-- Standardize Date Format

select SaleDateConverted, convert(Date,SaleDate)
from PortfolioProject.dbo.NashvilleHousing

alter table NashvilleHousing
add SaleDateConverted Date

Update NashvilleHousing
set SaleDateConverted = Convert(Date, SaleDate)

-- Populate Property Address data

select a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, isnull(a.PropertyAddress, b.PropertyAddress)
from PortfolioProject.dbo.NashvilleHousing a
join PortfolioProject.dbo.NashvilleHousing b
	on a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID]
Where a.PropertyAddress is null

Update a
set PropertyAddress = isnull(a.PropertyAddress, b.PropertyAddress)
from PortfolioProject.dbo.NashvilleHousing a
join PortfolioProject.dbo.NashvilleHousing b
	on a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID]
Where a.PropertyAddress is null



-- Breaking out Address into Indvidual Columns (Address, City, State)

Select PropertyAdress
From PortfolioProject.dbo.NashvilleHousing

Select
substring(propertyaddress, 1, charindex(',', propertyaddress) -1 ) as Address
, substring(propertyaddress, charindex(',', propertyaddress) + 1 , len(PropertyAddress) as Address


From PortfolioProject.dbo.NashvilleHousing

alter table NashvilleHousing
add PropertySplitAddress Nvarchar(255);

Update NashvilleHousing
set PropertySplitAddress = substring(propertyaddress, 1, charindex(',', propertyaddress) -1 )


alter table NashvilleHousing
add PropertySplitCity Nvarchar(255);

Update NashvilleHousing
set PropertySplitCity = substring(propertyaddress, charindex(',', propertyaddress) + 1 , len(PropertyAddress))


select OwnerAddress
from PortfolioProject.dbo.NashvilleHousing

select
parsename(Replace(OwnerAddress, ',', '.'), 3),

parsename(Replace(OwnerAddress, ',', '.'), 2),

parsename(Replace(OwnerAddress, ',', '.'), 1)
from PortfolioProject.dbo.NashvilleHousing






alter table NashvilleHousing
add ownerSplitAddress Nvarchar(255);

Update NashvilleHousing
set ownerSplitAddress = parsename(Replace(OwnerAddress, ',', '.'), 3)


alter table NashvilleHousing
add ownerSplitCity Nvarchar(255);

Update NashvilleHousing
set ownerSplitCity = parsename(Replace(OwnerAddress, ',', '.'), 2)

alter table NashvilleHousing
add ownerSplitState Nvarchar(255);

Update NashvilleHousing
set ownerSplitState = parsename(Replace(OwnerAddress, ',', '.'), 1)

Select *
From PortfolioProject.dbo.NashvilleHousing

-- Change Y and N to Yes and No in "Sold as Vacant" column

select distinct(SoldAsVacant), Count(SoldAsVacant)
From PortfolioProject.dbo.NashvilleHousing
Group by SoldAsVacant
order by 2


Select SoldAsVacant, 
Case when SoldAsVacant = 'Y' THEN 'Yes'
	 when SoldAsVacant = 'N' THEN 'No'
	 ELSE SoldAsVacant
	 END
From PortfolioProject.dbo.NashvilleHousing

Update NashvilleHousing
set SoldAsVacant = Case when SoldAsVacant = 'Y' THEN 'Yes'
	 when SoldAsVacant = 'N' THEN 'No'
	 ELSE SoldAsVacant
	 END


-- Removing Duplicates

with RowNumCTE AS(
Select *,
	row_number() over (
	partition by parcelid,
				 propertyaddress,
				 saleprice,
				 saledate,
				 legalreference
				 ORDER BY
					UniqueID
					) row_num


From PortfolioProject.dbo.NashvilleHousing
)
Delete
From RowNumCTE
Where row_num > 1



-- Delete Unused Columns

Select *
From PortfolioProject.dbo.NashvilleHousing

alter table PortfolioProject.dbo.NashvilleHousing
drop column owneraddress, taxdistrict, propertyaddress

alter table PortfolioProject.dbo.NashvilleHousing
drop column saledate

