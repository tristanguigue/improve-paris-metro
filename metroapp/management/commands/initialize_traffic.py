from django.core.management.base import BaseCommand

from metroapp.models import Edge, Line, StationLine


class Command(BaseCommand):
    help = 'Initialise traffic for each segment'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        Edge.objects.all().update(traffic=None)

        lines = Line.objects.all()
        for line in lines:
            stations = StationLine.objects.filter(line=line)
            termini = []

            for station in stations:
                if station.is_terminus:
                    termini.append(station)

            for terminus in termini:
                print(terminus.station.name)
                edge = terminus.outgoing_edges.first()
                occupancy = terminus.yearly_entries

                edge.navigate(occupancy, edge.routes)

            # edges = Edge.objects.filter(Q(stationA__in=stations) | Q(stationB__in=stations))

            # Get all stations and organise nodes/edges in graph structure

            # Breadth or depth first
            # For node calculate passengers that get out
            # For node calculate passengers that get in

            # Associate occupancy to segment

        self.stdout.write(self.style.SUCCESS('Traffic initialised'))