from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from devicemock.models.device import Device
from devicemock.serializers import DeviceSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('id')
    serializer_class = DeviceSerializer


class NodePaths(APIView):
    """
    Returns all unique paths from the devices table with hasChildren flag
    """
    def get(self, request):
        paths = list(Device.objects.values_list('path', flat=True).distinct().order_by('path'))
        
        # Extract all parent paths
        all_paths = set(paths)
        for path in paths:
            # Split path and build parent paths
            parts = [p for p in path.split('/') if p]  # Remove empty strings
            for i in range(1, len(parts)):
                parent = '/' + '/'.join(parts[:i]) + '/'
                all_paths.add(parent)
        
        # Convert to sorted list
        all_paths = sorted(list(all_paths))
        
        # Build response with hasChildren check
        result = []
        for path in all_paths:
            # Check if any other path starts with this path (is a subpath)
            has_children = any(
                other_path.startswith(path) and other_path != path 
                for other_path in all_paths
            )
            result.append({
                'path': path,
                'hasChildren': has_children
            })
        
        return Response({'nodes': result})