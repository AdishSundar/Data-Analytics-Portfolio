select *
from PortfolioProject..coviddeaths
order by 3,4

-- Looking at Covid Deaths Data

select location, date, total_cases, new_cases, total_deaths, population
from PortfolioProject..coviddeaths
order by 1,2

-- Looking at Total Cases vs. Total Deaths in America
-- Percent chance of dying from Covid
select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as DeathPercentage
from PortfolioProject..coviddeaths
where location like '%states%'
order by 1,2


-- Total Cases vs. Population in America
-- Percent of popoulation with Covid 
select location, date, total_cases, population, (total_cases/population)*100 as PopulationCovid
from PortfolioProject..coviddeaths
where location like '%states%'
order by 1,2


-- Looking at Countries with Highest Infection Rate compared to Population

select location, population, MAX(total_cases) as HighestCovidCount, MAX((total_cases/population))*100 as PopulationCovid
from portfolioproject..Coviddeaths
group by population, location 
order by populationcovid desc


-- Showing Countries with Highest Death Count by population
select location, MAX(cast(total_deaths as int)) as TotalDeathCount
from portfolioproject..Coviddeaths
where continent is not null
group by  location 
order by totaldeathcount desc

-- Looking at Continent deaths
select continent, MAX(cast(total_deaths as int)) as TotalDeathCount
from portfolioproject..Coviddeaths
where continent is not null
group by continent
order by totaldeathcount desc

-- global numbers

select date, sum(new_cases) as total_cases, sum(cast(new_deaths as int)) as total_deaths, SUM(cast(new_deaths as int))/sum(new_cases)*100 as DeathPercentage
from PortfolioProject..coviddeaths
where continent is not null
group by date
order by date, total_cases

select  sum(new_cases) as total_cases, sum(cast(new_deaths as int)) as total_deaths, SUM(cast(new_deaths as int))/sum(new_cases)*100 as DeathPercentage
from PortfolioProject..coviddeaths
where continent is not null


-- Combining Covid Vaccination data with Covid Death Data

select *
from PortfolioProject..coviddeaths dea
join PortfolioProject..covidvaccinations vac
	on dea.location = vac.location 
	and dea.date = vac.date

-- Looking at Total Population vs. Vaccinations

select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, sum(cast(vac.new_vaccinations as int)) over (partition by dea.location order by dea.location, dea.date) as RollingPeopleVaccinated
from PortfolioProject..coviddeaths dea
join PortfolioProject..covidvaccinations vac
	on dea.location = vac.location 
	and dea.date = vac.date
where dea.continent is not null
order by 2,3

with PopvsVac (Continent,Location,Date, Population, new_vaccinations, Rollingpeoplevaccinated)
as
(
select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, sum(cast(vac.new_vaccinations as int)) over (partition by dea.location order by dea.location, dea.date) as RollingPeopleVaccinated
from PortfolioProject..coviddeaths dea
join PortfolioProject..covidvaccinations vac
	on dea.location = vac.location 
	and dea.date = vac.date
where dea.continent is not null
)
select*, (Rollingpeoplevaccinated/Population)*100 as RollingPercentVaccinated
from popvsvac

-- temp table

Drop table if exists #PercentPopulationVaccinated
create table #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
date datetime,
population numeric,
new_vaccinations numeric,
rollingpeoplevaccinated numeric
)

insert into #PercentPopulationVaccinated
select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, sum(cast(vac.new_vaccinations as int)) over (partition by dea.location order by dea.location, dea.date) as RollingPeopleVaccinated
from PortfolioProject..coviddeaths dea
join PortfolioProject..covidvaccinations vac
	on dea.location = vac.location 
	and dea.date = vac.date
where dea.continent is not null

select*, (rollingpeoplevaccinated/population)*100 as RollingPercentVaccinated
from #PercentPopulationVaccinated

-- Creating View to store data for later visualizations

Create View PercentPopulationVaccinated as
select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, sum(cast(vac.new_vaccinations as int)) over (partition by dea.location order by dea.location, dea.date) as RollingPeopleVaccinated
from PortfolioProject..coviddeaths dea
join PortfolioProject..covidvaccinations vac
	on dea.location = vac.location 
	and dea.date = vac.date
where dea.continent is not null

Select *
From PercentPopulationVaccinated