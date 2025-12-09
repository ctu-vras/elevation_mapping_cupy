from ros2_numpy import numpify
import numpy as np
import struct
from sensor_msgs.msg import PointCloud2, PointField
import std_msgs.msg

def create_dummy_pointcloud():
    # Example data: 3 points (x, y, z)
    points = np.array([
        [1.0, 2.0, 3.0],
        [4.0, np.nan, 6.0],  # Include a NaN to test filtering
        [7.0, 8.0, 9.0]
    ], dtype=np.float32)

    # Pack into binary
    buffer = b''.join([struct.pack('fff', *p) for p in points])

    # Create PointCloud2 message
    msg = PointCloud2()
    msg.header = std_msgs.msg.Header()
    msg.header.frame_id = "map"

    msg.height = 1
    msg.width = points.shape[0]
    msg.is_dense = False  # allow NaN values
    msg.is_bigendian = False
    msg.point_step = 12  # 3 * 4 bytes
    msg.row_step = msg.point_step * msg.width
    msg.fields = [
        PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
        PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
        PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1)
    ]
    msg.data = buffer

    return msg

if __name__ == "__main__":
    import rclpy
    rclpy.init()
    pc_msg = create_dummy_pointcloud()
    points = numpify(pc_msg)

    # Extract XYZ and flatten
    xyz = np.stack([points['x'], points['y'], points['z']], axis=-1).reshape(-1, 3)

    # Apply mask to remove NaN rows
    mask = ~np.isnan(xyz).any(axis=1)
    filtered_xyz = xyz[mask]

    print("Original XYZ:")
    print(xyz)
    print("Mask:")
    print(mask)
    print("Filtered XYZ:")
    print(filtered_xyz)

