"""A python client for the stats.nba.com API."""

import requests


#  Constants - Taken from https://github.com/seemethere/nba_py/
BASE_URL = 'http://stats.nba.com/stats/{endpoint}'
HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'}


class Client():

    def _get_json(self, endpoint, params):

        res = requests.get(
            BASE_URL.format(endpoint=endpoint),
            params=params,
            headers=HEADERS
        )
        res.raise_for_status()
        return res.json()

    def allstarballotpredictor(
        self,
        pointcap,
        westplayer1,
        westplayer2,
        westplayer3,
        westplayer4,
        westplayer5,
        eastplayer1,
        eastplayer2,
        eastplayer3,
        eastplayer4,
        eastplayer5,
    ):
        """None."""
        params = {
            "PointCap": pointcap,
            "WestPlayer1": westplayer1,
            "WestPlayer2": westplayer2,
            "WestPlayer3": westplayer3,
            "WestPlayer4": westplayer4,
            "WestPlayer5": westplayer5,
            "EastPlayer1": eastplayer1,
            "EastPlayer2": eastplayer2,
            "EastPlayer3": eastplayer3,
            "EastPlayer4": eastplayer4,
            "EastPlayer5": eastplayer5,
        }
        return self._get_json("allstarballotpredictor", params)

    def boxscore(
        self,
        gameid,
        startperiod,
        endperiod,
        startrange,
        endrange,
        rangetype,
    ):
        """None."""
        params = {
            "GameID": gameid,
            "StartPeriod": startperiod,
            "EndPeriod": endperiod,
            "StartRange": startrange,
            "EndRange": endrange,
            "RangeType": rangetype,
        }
        return self._get_json("boxscore", params)

    def boxscoreadvanced(
        self,
        gameid,
        startperiod,
        endperiod,
        startrange,
        endrange,
        rangetype,
    ):
        """None."""
        params = {
            "GameID": gameid,
            "StartPeriod": startperiod,
            "EndPeriod": endperiod,
            "StartRange": startrange,
            "EndRange": endrange,
            "RangeType": rangetype,
        }
        return self._get_json("boxscoreadvanced", params)

    def boxscoreadvancedv2(
        self,
        gameid,
        startperiod,
        endperiod,
        startrange,
        endrange,
        rangetype,
    ):
        """None."""
        params = {
            "GameID": gameid,
            "StartPeriod": startperiod,
            "EndPeriod": endperiod,
            "StartRange": startrange,
            "EndRange": endrange,
            "RangeType": rangetype,
        }
        return self._get_json("boxscoreadvancedv2", params)

    def boxscorefourfactors(
        self,
        gameid,
        startperiod,
        endperiod,
        startrange,
        endrange,
        rangetype,
    ):
        """None."""
        params = {
            "GameID": gameid,
            "StartPeriod": startperiod,
            "EndPeriod": endperiod,
            "StartRange": startrange,
            "EndRange": endrange,
            "RangeType": rangetype,
        }
        return self._get_json("boxscorefourfactors", params)

    def boxscorefourfactorsv2(
        self,
        gameid,
        startperiod,
        endperiod,
        startrange,
        endrange,
        rangetype,
    ):
        """None."""
        params = {
            "GameID": gameid,
            "StartPeriod": startperiod,
            "EndPeriod": endperiod,
            "StartRange": startrange,
            "EndRange": endrange,
            "RangeType": rangetype,
        }
        return self._get_json("boxscorefourfactorsv2", params)

    def boxscoremisc(
        self,
        gameid,
        startperiod,
        endperiod,
        startrange,
        endrange,
        rangetype,
    ):
        """None."""
        params = {
            "GameID": gameid,
            "StartPeriod": startperiod,
            "EndPeriod": endperiod,
            "StartRange": startrange,
            "EndRange": endrange,
            "RangeType": rangetype,
        }
        return self._get_json("boxscoremisc", params)

    def boxscoremiscv2(
        self,
        gameid,
        startperiod,
        endperiod,
        startrange,
        endrange,
        rangetype,
    ):
        """None."""
        params = {
            "GameID": gameid,
            "StartPeriod": startperiod,
            "EndPeriod": endperiod,
            "StartRange": startrange,
            "EndRange": endrange,
            "RangeType": rangetype,
        }
        return self._get_json("boxscoremiscv2", params)

    def boxscoreplayertrackv2(
        self,
        gameid,
    ):
        """None."""
        params = {
            "GameID": gameid,
        }
        return self._get_json("boxscoreplayertrackv2", params)

    def boxscorescoring(
        self,
        gameid,
        startperiod,
        endperiod,
        startrange,
        endrange,
        rangetype,
    ):
        """None."""
        params = {
            "GameID": gameid,
            "StartPeriod": startperiod,
            "EndPeriod": endperiod,
            "StartRange": startrange,
            "EndRange": endrange,
            "RangeType": rangetype,
        }
        return self._get_json("boxscorescoring", params)

    def boxscorescoringv2(
        self,
        gameid,
        startperiod,
        endperiod,
        startrange,
        endrange,
        rangetype,
    ):
        """None."""
        params = {
            "GameID": gameid,
            "StartPeriod": startperiod,
            "EndPeriod": endperiod,
            "StartRange": startrange,
            "EndRange": endrange,
            "RangeType": rangetype,
        }
        return self._get_json("boxscorescoringv2", params)

    def boxscoresummaryv2(
        self,
        gameid,
    ):
        """None."""
        params = {
            "GameID": gameid,
        }
        return self._get_json("boxscoresummaryv2", params)

    def boxscoretraditionalv2(
        self,
        gameid,
        startperiod,
        endperiod,
        startrange,
        endrange,
        rangetype,
    ):
        """None."""
        params = {
            "GameID": gameid,
            "StartPeriod": startperiod,
            "EndPeriod": endperiod,
            "StartRange": startrange,
            "EndRange": endrange,
            "RangeType": rangetype,
        }
        return self._get_json("boxscoretraditionalv2", params)

    def boxscoreusage(
        self,
        gameid,
        startperiod,
        endperiod,
        startrange,
        endrange,
        rangetype,
    ):
        """None."""
        params = {
            "GameID": gameid,
            "StartPeriod": startperiod,
            "EndPeriod": endperiod,
            "StartRange": startrange,
            "EndRange": endrange,
            "RangeType": rangetype,
        }
        return self._get_json("boxscoreusage", params)

    def boxscoreusagev2(
        self,
        gameid,
        startperiod,
        endperiod,
        startrange,
        endrange,
        rangetype,
    ):
        """None."""
        params = {
            "GameID": gameid,
            "StartPeriod": startperiod,
            "EndPeriod": endperiod,
            "StartRange": startrange,
            "EndRange": endrange,
            "RangeType": rangetype,
        }
        return self._get_json("boxscoreusagev2", params)

    def commonteamyears(
        self,
        leagueid,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
        }
        return self._get_json("commonTeamYears", params)

    def commonallplayers(
        self,
        leagueid,
        season,
        isonlycurrentseason,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "Season": season,
            "IsOnlyCurrentSeason": isonlycurrentseason,
        }
        return self._get_json("commonallplayers", params)

    def commonplayerinfo(
        self,
        playerid,
    ):
        """None."""
        params = {
            "PlayerID": playerid,
        }
        return self._get_json("commonplayerinfo", params)

    def commonplayoffseries(
        self,
        leagueid,
        season,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "Season": season,
        }
        return self._get_json("commonplayoffseries", params)

    def commonteamroster(
        self,
        season,
        teamid,
    ):
        """None."""
        params = {
            "Season": season,
            "TeamID": teamid,
        }
        return self._get_json("commonteamroster", params)

    def draftcombinedrillresults(
        self,
        leagueid,
        seasonyear,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "SeasonYear": seasonyear,
        }
        return self._get_json("draftcombinedrillresults", params)

    def draftcombinenonstationaryshooting(
        self,
        leagueid,
        seasonyear,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "SeasonYear": seasonyear,
        }
        return self._get_json("draftcombinenonstationaryshooting", params)

    def draftcombineplayeranthro(
        self,
        leagueid,
        seasonyear,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "SeasonYear": seasonyear,
        }
        return self._get_json("draftcombineplayeranthro", params)

    def draftcombinespotshooting(
        self,
        leagueid,
        seasonyear,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "SeasonYear": seasonyear,
        }
        return self._get_json("draftcombinespotshooting", params)

    def draftcombinestats(
        self,
        leagueid,
        seasonyear,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "SeasonYear": seasonyear,
        }
        return self._get_json("draftcombinestats", params)

    def drafthistory(
        self,
        leagueid,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
        }
        return self._get_json("drafthistory", params)

    def franchisehistory(
        self,
        leagueid,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
        }
        return self._get_json("franchisehistory", params)

    def homepageleaders(
        self,
        statcategory,
        leagueid,
        season,
        seasontype,
        playerorteam,
        game,
        scope,
        player,
        scope,
    ):
        """None."""
        params = {
            "StatCategory": statcategory,
            "LeagueID": leagueid,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerOrTeam": playerorteam,
            "Game": game,
            "Scope": scope,
            "Player": player,
            "Scope": scope,
        }
        return self._get_json("homepageleaders", params)

    def homepagev2(
        self,
        stattype,
        leagueid,
        season,
        seasontype,
        playerorteam,
        game,
        scope,
        player,
        scope,
    ):
        """None."""
        params = {
            "StatType": stattype,
            "LeagueID": leagueid,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerOrTeam": playerorteam,
            "Game": game,
            "Scope": scope,
            "Player": player,
            "Scope": scope,
        }
        return self._get_json("homepagev2", params)

    def leaderstiles(
        self,
        stat,
        leagueid,
        season,
        seasontype,
        playerorteam,
        game,
        scope,
        player,
        scope,
    ):
        """None."""
        params = {
            "Stat": stat,
            "LeagueID": leagueid,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerOrTeam": playerorteam,
            "Game": game,
            "Scope": scope,
            "Player": player,
            "Scope": scope,
        }
        return self._get_json("leaderstiles", params)

    def leaguedashlineups(
        self,
        groupquantity,
        seasontype,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "GroupQuantity": groupquantity,
            "SeasonType": seasontype,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("leaguedashlineups", params)

    def leaguedashplayerbiostats(
        self,
        permode,
        leagueid,
        season,
        seasontype,
    ):
        """None."""
        params = {
            "PerMode": permode,
            "LeagueID": leagueid,
            "Season": season,
            "SeasonType": seasontype,
        }
        return self._get_json("leaguedashplayerbiostats", params)

    def leaguedashplayerclutch(
        self,
        clutchtime,
        aheadbehind,
        pointdiff,
        gamescope,
        playerexperience,
        playerposition,
        starterbench,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "ClutchTime": clutchtime,
            "AheadBehind": aheadbehind,
            "PointDiff": pointdiff,
            "GameScope": gamescope,
            "PlayerExperience": playerexperience,
            "PlayerPosition": playerposition,
            "StarterBench": starterbench,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("leaguedashplayerclutch", params)

    def leaguedashplayerptshot(
        self,
        leagueid,
        permode,
        season,
        seasontype,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "PerMode": permode,
            "Season": season,
            "SeasonType": seasontype,
        }
        return self._get_json("leaguedashplayerptshot", params)

    def leaguedashplayershotlocations(
        self,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
        distancerange,
        gamescope,
        playerexperience,
        playerposition,
        starterbench,
    ):
        """None."""
        params = {
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
            "DistanceRange": distancerange,
            "GameScope": gamescope,
            "PlayerExperience": playerexperience,
            "PlayerPosition": playerposition,
            "StarterBench": starterbench,
        }
        return self._get_json("leaguedashplayershotlocations", params)

    def leaguedashplayerstats(
        self,
        gamescope,
        playerexperience,
        playerposition,
        starterbench,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "GameScope": gamescope,
            "PlayerExperience": playerexperience,
            "PlayerPosition": playerposition,
            "StarterBench": starterbench,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("leaguedashplayerstats", params)

    def leaguedashptdefend(
        self,
        leagueid,
        permode,
        season,
        seasontype,
        defensecategory,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "PerMode": permode,
            "Season": season,
            "SeasonType": seasontype,
            "DefenseCategory": defensecategory,
        }
        return self._get_json("leaguedashptdefend", params)

    def leaguedashptteamdefend(
        self,
        leagueid,
        permode,
        season,
        seasontype,
        defensecategory,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "PerMode": permode,
            "Season": season,
            "SeasonType": seasontype,
            "DefenseCategory": defensecategory,
        }
        return self._get_json("leaguedashptteamdefend", params)

    def leaguedashteamclutch(
        self,
        clutchtime,
        aheadbehind,
        pointdiff,
        gamescope,
        playerexperience,
        playerposition,
        starterbench,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "ClutchTime": clutchtime,
            "AheadBehind": aheadbehind,
            "PointDiff": pointdiff,
            "GameScope": gamescope,
            "PlayerExperience": playerexperience,
            "PlayerPosition": playerposition,
            "StarterBench": starterbench,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("leaguedashteamclutch", params)

    def leaguedashteamptshot(
        self,
        leagueid,
        permode,
        season,
        seasontype,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "PerMode": permode,
            "Season": season,
            "SeasonType": seasontype,
        }
        return self._get_json("leaguedashteamptshot", params)

    def leaguedashteamshotlocations(
        self,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
        distancerange,
        gamescope,
        playerexperience,
        playerposition,
        starterbench,
    ):
        """None."""
        params = {
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
            "DistanceRange": distancerange,
            "GameScope": gamescope,
            "PlayerExperience": playerexperience,
            "PlayerPosition": playerposition,
            "StarterBench": starterbench,
        }
        return self._get_json("leaguedashteamshotlocations", params)

    def leaguedashteamstats(
        self,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("leaguedashteamstats", params)

    def leagueleaders(
        self,
        leagueid,
        permode,
        statcategory,
        season,
        seasontype,
        scope,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "PerMode": permode,
            "StatCategory": statcategory,
            "Season": season,
            "SeasonType": seasontype,
            "Scope": scope,
        }
        return self._get_json("leagueleaders", params)

    def playbyplay(
        self,
        gameid,
        startperiod,
        endperiod,
    ):
        """None."""
        params = {
            "GameID": gameid,
            "StartPeriod": startperiod,
            "EndPeriod": endperiod,
        }
        return self._get_json("playbyplay", params)

    def playbyplayv2(
        self,
        gameid,
        startperiod,
        endperiod,
    ):
        """None."""
        params = {
            "GameID": gameid,
            "StartPeriod": startperiod,
            "EndPeriod": endperiod,
        }
        return self._get_json("playbyplayv2", params)

    def playercareerstats(
        self,
        permode,
        playerid,
    ):
        """None."""
        params = {
            "PerMode": permode,
            "PlayerID": playerid,
        }
        return self._get_json("playercareerstats", params)

    def playercompare(
        self,
        playeridlist,
        vsplayeridlist,
        seasontype,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "PlayerIDList": playeridlist,
            "VsPlayerIDList": vsplayeridlist,
            "SeasonType": seasontype,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("playercompare", params)

    def playerdashboardbyclutch(
        self,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        playerid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerID": playerid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("playerdashboardbyclutch", params)

    def playerdashboardbygamesplits(
        self,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        playerid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerID": playerid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("playerdashboardbygamesplits", params)

    def playerdashboardbygeneralsplits(
        self,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        playerid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerID": playerid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("playerdashboardbygeneralsplits", params)

    def playerdashboardbylastngames(
        self,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        playerid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerID": playerid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("playerdashboardbylastngames", params)

    def playerdashboardbyopponent(
        self,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        playerid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerID": playerid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("playerdashboardbyopponent", params)

    def playerdashboardbyshootingsplits(
        self,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        playerid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerID": playerid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("playerdashboardbyshootingsplits", params)

    def playerdashboardbyteamperformance(
        self,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        playerid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerID": playerid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("playerdashboardbyteamperformance", params)

    def playerdashboardbyyearoveryear(
        self,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        playerid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerID": playerid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("playerdashboardbyyearoveryear", params)

    def playerdashptpass(
        self,
        permode,
        season,
        seasontype,
        playerid,
        teamid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        lastngames,
    ):
        """None."""
        params = {
            "PerMode": permode,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerID": playerid,
            "TeamID": teamid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "LastNGames": lastngames,
        }
        return self._get_json("playerdashptpass", params)

    def playerdashptreb(
        self,
        permode,
        season,
        seasontype,
        playerid,
        teamid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "PerMode": permode,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerID": playerid,
            "TeamID": teamid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("playerdashptreb", params)

    def playerdashptreboundlogs(
        self,
        season,
        seasontype,
        playerid,
        teamid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "Season": season,
            "SeasonType": seasontype,
            "PlayerID": playerid,
            "TeamID": teamid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("playerdashptreboundlogs", params)

    def playerdashptshotdefend(
        self,
        permode,
        season,
        seasontype,
        playerid,
        teamid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "PerMode": permode,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerID": playerid,
            "TeamID": teamid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("playerdashptshotdefend", params)

    def playerdashptshotlog(
        self,
        leagueid,
        season,
        seasontype,
        playerid,
        teamid,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerID": playerid,
            "TeamID": teamid,
        }
        return self._get_json("playerdashptshotlog", params)

    def playerdashptshots(
        self,
        permode,
        season,
        seasontype,
        playerid,
        teamid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "PerMode": permode,
            "Season": season,
            "SeasonType": seasontype,
            "PlayerID": playerid,
            "TeamID": teamid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("playerdashptshots", params)

    def playergamelog(
        self,
        playerid,
        season,
        seasontype,
    ):
        """None."""
        params = {
            "PlayerID": playerid,
            "Season": season,
            "SeasonType": seasontype,
        }
        return self._get_json("playergamelog", params)

    def playerprofile(
        self,
        leagueid,
        playerid,
        season,
        seasontype,
        graphstartseason,
        graphendseason,
        graphstat,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "PlayerID": playerid,
            "Season": season,
            "SeasonType": seasontype,
            "GraphStartSeason": graphstartseason,
            "GraphEndSeason": graphendseason,
            "GraphStat": graphstat,
        }
        return self._get_json("playerprofile", params)

    def playerprofilev2(
        self,
        permode,
        playerid,
    ):
        """None."""
        params = {
            "PerMode": permode,
            "PlayerID": playerid,
        }
        return self._get_json("playerprofilev2", params)

    def playersvsplayers(
        self,
        playerteamid,
        playerid1,
        playerid2,
        playerid3,
        playerid4,
        playerid5,
        vsteamid,
        vsplayerid1,
        vsplayerid2,
        vsplayerid3,
        vsplayerid4,
        vsplayerid5,
        seasontype,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "PlayerTeamID": playerteamid,
            "PlayerID1": playerid1,
            "PlayerID2": playerid2,
            "PlayerID3": playerid3,
            "PlayerID4": playerid4,
            "PlayerID5": playerid5,
            "VsTeamID": vsteamid,
            "VsPlayerID1": vsplayerid1,
            "VsPlayerID2": vsplayerid2,
            "VsPlayerID3": vsplayerid3,
            "VsPlayerID4": vsplayerid4,
            "VsPlayerID5": vsplayerid5,
            "SeasonType": seasontype,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("playersvsplayers", params)

    def playervsplayer(
        self,
        playerid,
        vsplayerid,
        seasontype,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "PlayerID": playerid,
            "VsPlayerID": vsplayerid,
            "SeasonType": seasontype,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("playervsplayer", params)

    def playoffpicture(
        self,
        leagueid,
        seasonid,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "SeasonID": seasonid,
        }
        return self._get_json("playoffpicture", params)

    def scoreboard(
        self,
        gamedate,
        leagueid,
        dayoffset,
    ):
        """None."""
        params = {
            "GameDate": gamedate,
            "LeagueID": leagueid,
            "DayOffset": dayoffset,
        }
        return self._get_json("scoreboard", params)

    def scoreboardv2(
        self,
        gamedate,
        leagueid,
        dayoffset,
    ):
        """None."""
        params = {
            "GameDate": gamedate,
            "LeagueID": leagueid,
            "DayOffset": dayoffset,
        }
        return self._get_json("scoreboardV2", params)

    def shotchartdetail(
        self,
        seasontype,
        teamid,
        playerid,
        gameid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        position,
        rookieyear,
        gamesegment,
        period,
        lastngames,
        contextmeasure,
    ):
        """None."""
        params = {
            "SeasonType": seasontype,
            "TeamID": teamid,
            "PlayerID": playerid,
            "GameID": gameid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "Position": position,
            "RookieYear": rookieyear,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
            "ContextMeasure": contextmeasure,
        }
        return self._get_json("shotchartdetail", params)

    def shotchartlineupdetail(
        self,
        leagueid,
        season,
        seasontype,
        teamid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
        gameid,
        group_id,
        contextmeasure,
        contextfilter,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "Season": season,
            "SeasonType": seasontype,
            "TeamID": teamid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
            "GameID": gameid,
            "GROUP_ID": group_id,
            "ContextMeasure": contextmeasure,
            "ContextFilter": contextfilter,
        }
        return self._get_json("shotchartlineupdetail", params)

    def teamdashboardbyclutch(
        self,
        teamid,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "TeamID": teamid,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("teamdashboardbyclutch", params)

    def teamdashboardbygamesplits(
        self,
        teamid,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "TeamID": teamid,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("teamdashboardbygamesplits", params)

    def teamdashboardbygeneralsplits(
        self,
        seasontype,
        teamid,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "SeasonType": seasontype,
            "TeamID": teamid,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("teamdashboardbygeneralsplits", params)

    def teamdashboardbylastngames(
        self,
        teamid,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "TeamID": teamid,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("teamdashboardbylastngames", params)

    def teamdashboardbyopponent(
        self,
        teamid,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "TeamID": teamid,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("teamdashboardbyopponent", params)

    def teamdashboardbyshootingsplits(
        self,
        teamid,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "TeamID": teamid,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("teamdashboardbyshootingsplits", params)

    def teamdashboardbyteamperformance(
        self,
        teamid,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "TeamID": teamid,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("teamdashboardbyteamperformance", params)

    def teamdashboardbyyearoveryear(
        self,
        teamid,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "TeamID": teamid,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("teamdashboardbyyearoveryear", params)

    def teamdashlineups(
        self,
        groupquantity,
        gameid,
        seasontype,
        teamid,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "GroupQuantity": groupquantity,
            "GameID": gameid,
            "SeasonType": seasontype,
            "TeamID": teamid,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("teamdashlineups", params)

    def teamdashptpass(
        self,
        permode,
        season,
        seasontype,
        teamid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        lastngames,
    ):
        """None."""
        params = {
            "PerMode": permode,
            "Season": season,
            "SeasonType": seasontype,
            "TeamID": teamid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "LastNGames": lastngames,
        }
        return self._get_json("teamdashptpass", params)

    def teamdashptreb(
        self,
        permode,
        season,
        seasontype,
        teamid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "PerMode": permode,
            "Season": season,
            "SeasonType": seasontype,
            "TeamID": teamid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("teamdashptreb", params)

    def teamdashptshots(
        self,
        permode,
        season,
        seasontype,
        teamid,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "PerMode": permode,
            "Season": season,
            "SeasonType": seasontype,
            "TeamID": teamid,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("teamdashptshots", params)

    def teamgamelog(
        self,
        teamid,
        season,
        seasontype,
    ):
        """None."""
        params = {
            "TeamID": teamid,
            "Season": season,
            "SeasonType": seasontype,
        }
        return self._get_json("teamgamelog", params)

    def teaminfocommon(
        self,
        season,
        teamid,
        leagueid,
        seasontype,
    ):
        """None."""
        params = {
            "Season": season,
            "TeamID": teamid,
            "LeagueID": leagueid,
            "SeasonType": seasontype,
        }
        return self._get_json("teaminfocommon", params)

    def teamplayerdashboard(
        self,
        seasontype,
        teamid,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "SeasonType": seasontype,
            "TeamID": teamid,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("teamplayerdashboard", params)

    def teamplayeronoffdetails(
        self,
        teamid,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "TeamID": teamid,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("teamplayeronoffdetails", params)

    def teamplayeronoffsummary(
        self,
        teamid,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        seasontype,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "TeamID": teamid,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "SeasonType": seasontype,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("teamplayeronoffsummary", params)

    def teamvsplayer(
        self,
        teamid,
        vsplayerid,
        seasontype,
        measuretype,
        permode,
        plusminus,
        paceadjust,
        rank,
        season,
        outcome,
        location,
        month,
        seasonsegment,
        datefrom,
        dateto,
        opponentteamid,
        vsconference,
        vsdivision,
        gamesegment,
        period,
        lastngames,
    ):
        """None."""
        params = {
            "TeamID": teamid,
            "VsPlayerID": vsplayerid,
            "SeasonType": seasontype,
            "MeasureType": measuretype,
            "PerMode": permode,
            "PlusMinus": plusminus,
            "PaceAdjust": paceadjust,
            "Rank": rank,
            "Season": season,
            "Outcome": outcome,
            "Location": location,
            "Month": month,
            "SeasonSegment": seasonsegment,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "OpponentTeamID": opponentteamid,
            "VsConference": vsconference,
            "VsDivision": vsdivision,
            "GameSegment": gamesegment,
            "Period": period,
            "LastNGames": lastngames,
        }
        return self._get_json("teamvsplayer", params)

    def teamyearbyyearstats(
        self,
        leagueid,
        seasontype,
        permode,
        teamid,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "SeasonType": seasontype,
            "PerMode": permode,
            "TeamID": teamid,
        }
        return self._get_json("teamyearbyyearstats", params)

    def videostatus(
        self,
        leagueid,
        gamedate,
    ):
        """None."""
        params = {
            "LeagueID": leagueid,
            "GameDate": gamedate,
        }
        return self._get_json("videoStatus", params)
