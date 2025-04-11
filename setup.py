from setuptools import find_packages, setup

package_name = 'motoman_ma2010_support'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch',
            ['launch/robot_state_visualize_ma2010.launch.py',
             'launch/load_ma2010.launch.py',]),
        ('share/' + package_name + '/urdf',
            ['urdf/ma2010.xacro',
             'urdf/ma2010_macro.xacro']),
        ('share/' + package_name + '/meshes/ma2010/visual',
            ['meshes/ma2010/visual/base_link.stl',
             'meshes/ma2010/visual/link_1_s.stl',
             'meshes/ma2010/visual/link_2_l.stl',
             'meshes/ma2010/visual/link_3_u.stl',
             'meshes/ma2010/visual/link_4_r.stl',
             'meshes/ma2010/visual/link_5_b.stl',
             'meshes/ma2010/visual/link_6_t.stl',]),
        ('share/' + package_name + '/meshes/ma2010/collision',
            ['meshes/ma2010/collision/base_link.stl',
             'meshes/ma2010/collision/link_1_s.stl',
             'meshes/ma2010/collision/link_2_l.stl',
             'meshes/ma2010/collision/link_3_u.stl',
             'meshes/ma2010/collision/link_4_r.stl',
             'meshes/ma2010/collision/link_5_b.stl',
             'meshes/ma2010/collision/link_6_t.stl',]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='julien',
    maintainer_email='julien.livet@free.fr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
