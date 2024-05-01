import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_map/flutter_map.dart';

class TileLayerControl extends StatelessWidget with FletStoreMixin {
  final Control? parent;
  final Control control;
  final FletControlBackend backend;

  const TileLayerControl(
      {super.key,
      required this.parent,
      required this.control,
      required this.backend});

  @override
  Widget build(BuildContext context) {
    debugPrint("TileLayerControl build: ${control.id} (${control.hashCode})");

    return withPageArgs((context, pageArgs) {
      var errorImageSrc = control.attrString("errorImageSrc");

      ImageProvider<Object>? errorImage;

      if (errorImageSrc != null) {
        var assetSrc =
            getAssetSrc((errorImageSrc), pageArgs.pageUri!, pageArgs.assetsDir);

        if (assetSrc.isFile) {
          // from File
          errorImage = AssetImage(assetSrc.path);
        } else {
          // URL
          errorImage = NetworkImage(assetSrc.path);
        }
      }
      Widget tile = TileLayer(
          urlTemplate: control.attrString("urlTemplate", "")!,
          fallbackUrl: control.attrString("fallbackUrl", "")!,
          tileSize: control.attrDouble("tileSize", 256)!,
          minNativeZoom: control.attrInt("minNativeZoom", 0)!,
          maxNativeZoom: control.attrInt("maxNativeZoom", 19)!,
          zoomReverse: control.attrBool("zoomReverse", false)!,
          zoomOffset: control.attrDouble("zoomOffset", 0)!,
          // additionalOptions: ,
          // subdomains: ,
          keepBuffer: control.attrInt("keepBuffer", 2)!,
          panBuffer: control.attrInt("panBuffer", 1)!,
          tms: control.attrBool("tms", false)!,
          maxZoom: control.attrDouble("maxZoom", double.infinity)!,
          minZoom: control.attrDouble("minZoom", 0)!,
          errorImage: errorImage,
          errorTileCallback: (TileImage t, Object o, StackTrace? s) {
            backend.triggerControlEvent(control.id, "imageError");
          });

      return constrainedControl(context, tile, parent, control);
    });
  }
}
